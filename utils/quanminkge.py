import re

import requests

HEADERS = {
    "accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "zh-CN,zh;q=0.9",
    "cache-control":
    "max-age=0",
    "sec-fetch-mode":
    "navigate",
    "sec-fetch-site":
    "none",
    "upgrade-insecure-requests":
    "1",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
}

SINGER_PATTERN = r',"nick":"(.*?)",'
SONG_NAME_PATTERN = r'"song_name":"(.*?)",'
PLAY_URL_PATTERN = r'"playurl":"(.*?)",'


def get(share_url):
    '''
    return {
        singer:
        song_name:
        play_url:
    }
    '''
    with requests.get(url=share_url, headers=HEADERS, timeout=50) as rep:
        if rep.status_code == 200:
            html = rep.text
            singer = re.findall(SINGER_PATTERN, html)[0]
            song_name = re.findall(SONG_NAME_PATTERN, html)[0]
            play_url = re.findall(PLAY_URL_PATTERN, html)[0]
        else:
            singer = ""
            song_name = ""
            play_url = ""

    return {
        "singer": singer,
        "song_name": song_name,
        "play_url": play_url,
    }


if __name__ == "__main__":
    data = get(input("share_url: \n"))
    print(data)