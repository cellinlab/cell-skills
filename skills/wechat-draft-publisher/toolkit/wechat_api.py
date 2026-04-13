"""
WeChat Official Account API helpers for publish-only workflows.
"""

from __future__ import annotations

import mimetypes
import time
from dataclasses import dataclass
from pathlib import Path

import requests


_TOKEN_CACHE: dict[str, "TokenResult"] = {}


@dataclass
class TokenResult:
    access_token: str
    expires_at: float


@dataclass
class UploadCoverResult:
    media_id: str
    media_type: str


def get_access_token(appid: str, secret: str, force_refresh: bool = False) -> str:
    now = time.time()

    if not force_refresh and appid in _TOKEN_CACHE:
        cached = _TOKEN_CACHE[appid]
        if now < cached.expires_at:
            return cached.access_token

    response = requests.get(
        "https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": appid,
            "secret": secret,
        },
        timeout=20,
    )
    data = response.json()

    if "access_token" not in data:
        raise ValueError(
            f"WeChat API error: errcode={data.get('errcode', 'unknown')}, "
            f"errmsg={data.get('errmsg', 'unknown error')}"
        )

    access_token = str(data["access_token"])
    expires_in = int(data.get("expires_in", 7200))
    _TOKEN_CACHE[appid] = TokenResult(access_token=access_token, expires_at=now + expires_in - 300)
    return access_token


def upload_image(access_token: str, image_path: str) -> str:
    path = Path(image_path)
    content_type = _guess_content_type(path)

    with path.open("rb") as file_handle:
        response = requests.post(
            "https://api.weixin.qq.com/cgi-bin/media/uploadimg",
            params={"access_token": access_token},
            files={"media": (path.name, file_handle, content_type)},
            timeout=60,
        )

    data = response.json()
    if "url" not in data:
        raise ValueError(
            f"WeChat upload_image error: errcode={data.get('errcode', 'unknown')}, "
            f"errmsg={data.get('errmsg', 'unknown error')}"
        )

    return str(data["url"])


def upload_cover(access_token: str, image_path: str, preferred_type: str = "thumb") -> UploadCoverResult:
    attempts = _cover_media_attempts(preferred_type)
    errors: list[str] = []

    for media_type in attempts:
        path = Path(image_path)
        content_type = _guess_content_type(path)
        with path.open("rb") as file_handle:
            response = requests.post(
                "https://api.weixin.qq.com/cgi-bin/material/add_material",
                params={"access_token": access_token, "type": media_type},
                files={"media": (path.name, file_handle, content_type)},
                timeout=60,
            )
        data = response.json()
        if "media_id" in data:
            return UploadCoverResult(media_id=str(data["media_id"]), media_type=media_type)

        errors.append(
            f"type={media_type}: errcode={data.get('errcode', 'unknown')}, "
            f"errmsg={data.get('errmsg', 'unknown error')}"
        )

    raise ValueError("WeChat upload_cover error: " + " | ".join(errors))


def get_public_ip() -> str:
    for url in ("https://ifconfig.me", "https://api.ipify.org"):
        try:
            response = requests.get(url, timeout=10)
            text = response.text.strip()
            if text:
                return text
        except Exception:
            continue
    raise ValueError("Unable to determine public IP from fallback services")


def _guess_content_type(path: Path) -> str:
    content_type, _ = mimetypes.guess_type(str(path))
    return content_type or "application/octet-stream"


def _cover_media_attempts(preferred_type: str) -> list[str]:
    preferred = preferred_type.strip().lower() if preferred_type else "thumb"
    if preferred == "image":
        return ["image", "thumb"]
    return ["thumb", "image"]
