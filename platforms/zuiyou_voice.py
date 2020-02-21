import json
from urllib.parse import urlparse

import requests


def get(url: str) -> dict:
    """
    Args:
        url: the share url
    Returns:
        {
            voice_text:
            uri:
            org_uri:
        }
    """
    headers = {
        "Connection": "keep-alive",
        "Content-Length": "209",
        "Content-Type": "text/plain;charset=UTF-8",
        "Cookie": "Hm_lvt_414bd23f4090657a5e2034429c836cca=1582267903; Hm_lpvt_414bd23f4090657a5e2034429c836cca=1582268032",
        "Host": "share.izuiyou.com",
        "Origin": "https://share.izuiyou.com",
        "Referer": url,
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    post_url = "https://share.izuiyou.com/api/review/share_review"

    path = urlparse(url).path
    temp = path.split("/")
    pid = temp[-2]
    rid = temp[-1]

    payload = {
        "h_av": "3.0",
        "h_dt": 9,
        "h_nt": 9,
        "h_ch": "web_app",
        "ua":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "pid": f"{pid}",
        "rid": f"{rid}"
    }
    rep = requests.post(post_url, data=json.dumps(payload), headers=headers, timeout=20)
    if rep.status_code == 200:
        data = rep.json()
        try:
            audio_info = data.get("data").get("review").get("audio")
            voice_text = audio_info.get("voice_text")
            uri = audio_info.get("uri")
            org_uri = audio_info.get("org_uri")
        except AttributeError:
            voice_text = ""
            uri = ""
            org_uri = ""
    else:
        voice_text = ""
        uri = ""
        org_uri = ""

    play_host = "http://tbvideo.ixiaochuan.cn/"
    return {
        "voice_text": voice_text,
        "uri": play_host + uri,
        "org_uri": play_host + org_uri
    }


if __name__ == "__main__":
    url = "https://share.izuiyou.com/review/160475367/1464651064?zy_to=applink&to=applink"
    print(get(url))