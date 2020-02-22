import re

import requests as rs


def get(url: str) -> dict:
    """
    Args:
        url: the share url
        https://www.zhihu.com/zvideo/**********
        https://www.zhihu.com/answer/**********
    Returns:
        a dict{
            urls: []
        }
    """
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",}
    video_info_url = "https://lens.zhihu.com/api/v4/videos/{id}"

    ids = []
    urls = []

    rep = rs.get(url, headers=headers)
    if rep.status_code == 200:
        ids = re.findall(r'https://www.zhihu.com/video/(\d{1,})', rep.text)

    if ids:
        for id in ids:
            rep = rs.get(video_info_url.format(id=id), headers=headers)
            if rep.status_code == 200:
                data = rep.json()
                playlist = data.get("playlist")
                temp = playlist.get("HD") or playlist.get("SD") or playlist.get("LD")
                if temp:
                    url = temp.get("play_url")
                    urls.append(url)

    return {"urls": urls}


if __name__ == "__main__":
    url = input("url: ")
    print(get(url))