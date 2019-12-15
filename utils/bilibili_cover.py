import re
import requests


def get(url: str) -> dict:
    '''
    :url: video url
    :return:
        {'cover_url': cover_url} or {'cover_url': ''}
    '''
    HEADERS = {
        "user-agent":
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Referer": "https://m.bilibili.com/",
    }
    ERROR = {'cover_url': ''}  # 只要有不对劲的时候就返回这个东东

    # 处理一下视频地址
    if not url:
        return ERROR

    try:
        av_number_pattern = r'av([0-9]*)'
        av = re.findall(av_number_pattern, url)[0]
        url = f'https://www.bilibili.com/video/av{av}'
    except:
        return ERROR

    with requests.get(url, headers=HEADERS, timeout=18) as rep:
        cover_pattern = r'<meta property="og:image" content="(http.*?)"/>'
        if rep.status_code == 200:
            cover_url = re.findall(cover_pattern, rep.text)[0]
            if '@' in cover_url:
                cover_url = cover_url[:cover_url.index('@')]
            return {
                'cover_url': cover_url,
            }
        else:
            return ERROR


if __name__ == "__main__":
    url = "https://www.bilibili.com/video/av78638178"
    # url = input('input the url: ')
    print(get(url))