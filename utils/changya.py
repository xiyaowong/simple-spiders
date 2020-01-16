import re

import requests

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
}

AUDIO_URL_PATTERN = r'<audio src="(http://cdn.singroom.i52hz.com/.*?)" preload="metadata"'
AUTHOR_PATTERN = r'"nickname":"(.*?)",'
AUDIO_NAME_PATTERN = r'"songName":"(.*?)",'


def get(url):
    '''
    return {
        author:
        audio_name:
        audio_url:
    }
    '''
    with requests.get(url, headers=HEADERS, timeout=50) as rep:
        if rep.status_code == 200:
            html = rep.text
            author = re.findall(AUTHOR_PATTERN, html)[0]
            audio_name = re.findall(AUDIO_NAME_PATTERN, html)[0]
            audio_url = re.findall(AUDIO_URL_PATTERN, html)[0]
        else:
            author = audio_name = audio_url = ""

    return {
        "author": author,
        "audio_name": audio_name,
        "audio_url":audio_url,
    }


if __name__ == "__main__":
    data = get(input("url: "))
    print(data)