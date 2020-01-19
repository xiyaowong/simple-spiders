# 常用的处理函数

import requests


def get_origin_location(url, headers=None) -> str:
    '''
    短链接转成原始长链接
    '''
    if headers:
        headers = headers
    else:
        headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        }

    with requests.get(url, headers=headers) as rep:
        if rep.status_code == 200:
            return rep.url
        else:
            return url


if __name__ == "__main__":
    print(get_origin_location(input('url: ')))
