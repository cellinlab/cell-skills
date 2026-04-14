#!/usr/bin/env python3
"""
Export X/Twitter cookies from local browsers to Playwright storage state JSON.
"""

from __future__ import annotations

import argparse
import json
import sys
from http.cookiejar import Cookie
from pathlib import Path


TARGET_DOMAINS = ("x.com", "twitter.com")


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


def main() -> int:
    parser = argparse.ArgumentParser(description="Export X/Twitter cookies to Playwright storage state")
    parser.add_argument(
        "--browser",
        action="append",
        choices=["chrome", "chromium", "edge", "firefox", "opera", "brave"],
        help="Browser(s) to read from. Defaults to chrome. Pass multiple times to expand.",
    )
    parser.add_argument("--output", "-o", default="/tmp/x-storage-state.json", help="Output JSON path")
    parser.add_argument("--allow-empty", action="store_true", help="Write an empty storage state instead of failing")
    args = parser.parse_args()

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
        },
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(storage_state, ensure_ascii=False, indent=2), encoding="utf-8")
    print(str(output_path))
    print(f"cookies={len(cookies)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
