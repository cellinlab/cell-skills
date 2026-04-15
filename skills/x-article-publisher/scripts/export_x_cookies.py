#!/usr/bin/env python3
"""
Export X/Twitter cookies from local browsers to Playwright storage state JSON.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from http.cookiejar import Cookie
from pathlib import Path


TARGET_DOMAINS = ("x.com", "twitter.com")
AUTH_COOKIE_NAMES = ("auth_token", "ct0")
DEFAULT_CACHE_ROOT = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
DEFAULT_CACHE_PATH = DEFAULT_CACHE_ROOT / "x-article-publisher" / "x-storage-state.json"


def normalize_same_site(raw_value: str | None) -> str:
    if not raw_value:
        return "Lax"
    value = raw_value.strip().lower()
    if value == "strict":
        return "Strict"
    if value == "none":
        return "None"
    return "Lax"


def cookie_to_playwright(cookie: Cookie) -> dict:
    rest = getattr(cookie, "_rest", {}) or {}
    same_site = normalize_same_site(rest.get("SameSite") or rest.get("samesite"))
    expires = float(cookie.expires) if cookie.expires is not None else -1
    return {
        "name": cookie.name,
        "value": cookie.value,
        "domain": cookie.domain,
        "path": cookie.path or "/",
        "expires": expires,
        "httpOnly": bool("HttpOnly" in rest or "httponly" in rest or cookie.has_nonstandard_attr("HttpOnly")),
        "secure": bool(cookie.secure),
        "sameSite": same_site,
    }


def matches_x_domain(cookie: Cookie) -> bool:
    domain = (cookie.domain or "").lower()
    if domain.startswith("."):
        domain = domain[1:]
    return any(domain == target or domain.endswith(f".{target}") for target in TARGET_DOMAINS)


def load_browser_cookies(browser_name: str, domain_name: str):
    try:
        import browser_cookie3
    except ImportError:
        print("Error: browser-cookie3 not installed. Run: pip install browser-cookie3", file=sys.stderr)
        raise SystemExit(1)

    loaders = {
        "chrome": browser_cookie3.chrome,
        "chromium": browser_cookie3.chromium,
        "edge": browser_cookie3.edge,
        "firefox": browser_cookie3.firefox,
        "opera": browser_cookie3.opera,
        "brave": browser_cookie3.brave if hasattr(browser_cookie3, "brave") else browser_cookie3.chrome,
    }

    if browser_name not in loaders:
        raise ValueError(f"Unsupported browser: {browser_name}")

    return loaders[browser_name](domain_name=domain_name)


def gather_cookies(browser_names: list[str]) -> tuple[list[dict], dict[str, int]]:
    seen: set[tuple[str, str, str, str]] = set()
    exported: list[dict] = []
    counts: dict[str, int] = {}

    for browser_name in browser_names:
        browser_count = 0
        for domain_name in TARGET_DOMAINS:
            try:
                cookie_jar = load_browser_cookies(browser_name, domain_name)
            except Exception as exc:
                if browser_count == 0:
                    counts[browser_name] = -1
                print(
                    f"[export_x_cookies] Skipping {browser_name} ({domain_name}): {exc}",
                    file=sys.stderr,
                )
                continue

            for cookie in cookie_jar:
                if not matches_x_domain(cookie):
                    continue
                key = (cookie.domain, cookie.path, cookie.name, cookie.value)
                if key in seen:
                    continue
                seen.add(key)
                exported.append(cookie_to_playwright(cookie))
                browser_count += 1

        counts[browser_name] = browser_count

    return exported, counts


def is_cache_valid(cache_path: Path, max_age_hours: float = 12.0) -> bool:
    if not cache_path.exists():
        return False

    age_hours = (time.time() - cache_path.stat().st_mtime) / 3600
    if age_hours > max_age_hours:
        return False

    try:
        state = json.loads(cache_path.read_text(encoding="utf-8"))
    except Exception:
        return False

    cookies = {cookie.get("name"): cookie for cookie in state.get("cookies", [])}
    now = time.time()
    for name in AUTH_COOKIE_NAMES:
        cookie = cookies.get(name)
        if not cookie:
            return False

        expires = cookie.get("expires", -1)
        if isinstance(expires, (int, float)) and expires != -1 and expires < now:
            return False

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Export X/Twitter cookies to Playwright storage state")
    parser.add_argument(
        "--browser",
        action="append",
        choices=["chrome", "chromium", "edge", "firefox", "opera", "brave"],
        help="Browser(s) to read from. Defaults to chrome. Pass multiple times to expand.",
    )
    parser.add_argument("--output", "-o", default=str(DEFAULT_CACHE_PATH), help="Output JSON path")
    parser.add_argument("--allow-empty", action="store_true", help="Write an empty storage state instead of failing")
    parser.add_argument(
        "--use-cache",
        dest="use_cache",
        action="store_true",
        default=True,
        help="Reuse a valid cached storage state when possible. Enabled by default.",
    )
    parser.add_argument(
        "--no-cache",
        dest="use_cache",
        action="store_false",
        help="Ignore cached storage state and export fresh cookies from the browser.",
    )
    parser.add_argument(
        "--max-age-hours",
        type=float,
        default=12.0,
        help="Maximum cache age in hours before forcing a fresh export.",
    )
    args = parser.parse_args()

    output_path = Path(args.output).expanduser()
    if args.use_cache and is_cache_valid(output_path, max_age_hours=args.max_age_hours):
        print(str(output_path))
        print("cookies=cached")
        return 0

    browsers = args.browser or ["chrome"]
    cookies, counts = gather_cookies(browsers)

    if not cookies and not args.allow_empty:
        print("Error: no X/Twitter cookies found in selected browsers", file=sys.stderr)
        return 1

    storage_state = {
        "cookies": cookies,
        "origins": [],
        "meta": {
            "browsers": browsers,
            "counts": counts,
            "generated_at": int(time.time()),
        },
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(storage_state, ensure_ascii=False, indent=2), encoding="utf-8")
    print(str(output_path))
    print(f"cookies={len(cookies)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
