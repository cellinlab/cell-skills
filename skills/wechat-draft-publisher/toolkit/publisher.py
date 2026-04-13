"""
WeChat draft creation wrapper.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class DraftResult:
    media_id: str


def create_draft(
    access_token: str,
    title: str,
    html: str,
    digest: str,
    thumb_media_id: Optional[str] = None,
    author: Optional[str] = None,
) -> DraftResult:
    article: dict[str, object] = {
        "title": title,
        "author": author or "",
        "digest": digest,
        "content": html,
        "show_cover_pic": 0,
    }

    if thumb_media_id:
        article["thumb_media_id"] = thumb_media_id

    response = requests.post(
        "https://api.weixin.qq.com/cgi-bin/draft/add",
        params={"access_token": access_token},
        data=json.dumps({"articles": [article]}, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=60,
    )
    data = response.json()

    errcode = data.get("errcode", 0)
    if errcode != 0:
        raise ValueError(
            f"WeChat create_draft error: errcode={errcode}, errmsg={data.get('errmsg', 'unknown error')}"
        )

    media_id = data.get("media_id")
    if not media_id:
        raise ValueError(f"WeChat create_draft error: missing media_id in response: {data}")

    return DraftResult(media_id=str(media_id))
