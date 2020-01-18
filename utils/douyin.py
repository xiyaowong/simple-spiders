import re

import requests

HEADERS = {
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding':
    'gzip, deflate, br',
    'accept-language':
    'zh-CN,zh;q=0.9',
    'cache-control':
    'max-age=0',
    'upgrade-insecure-requests':
    '1',
    'user-agent':
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

TITLE_PATTERN = r'<div class="user-title">(.*?)</div>'
PLAY_URL_PATTERN = r'<video id="theVideo" class="video-player" src="(.*?)" preload'


def get(share_url) -> dict:
    '''
    return {
        video_name:
        video_url:
    }
    '''
    # get share_url location
    with requests.get(share_url, headers=HEADERS, timeout=30) as rep:
        share_url = rep.headers.get('location', share_url)
        print(share_url)

    # get html_text
    with requests.get(share_url, headers=HEADERS, timeout=30) as rep:
        html_text = rep.text
        print(html_text)

    try:
        title = re.findall(TITLE_PATTERN, html_text)[0]
        play_url = re.findall(PLAY_URL_PATTERN, html_text)[0].replace('playwm', 'play')
        print(title, play_url)
    except:
        title = ''
        play_url = ''


    # get video_url
    if play_url:
        with requests.get(play_url, headers=HEADERS, allow_redirects=False, timeout=30) as rep:
            print(rep.headers)
            video_url = rep.headers.get('location', '')
    else:
        video_url = ''

    return {
        'video_name': title,
        'video_url': video_url,
    }


if __name__ == "__main__":
    data = get(input('share url: '))
    print(data)