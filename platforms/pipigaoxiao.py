import json

import requests

HEADERS = {
    "Host": "share.ippzone.com",
    "Connection": "keep-alive",
    "Content-Length": "45",
    "Origin": "http://share.ippzone.com",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    "Content-Type": "text/plain;charset=UTF-8",
    "Accept": "*/*",
    "Referer": "http://share.ippzone.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

POST_URL = "http://share.ippzone.com/ppapi/share/fetch_content"


def get(url: str) -> dict:
    '''
    return {
        play_url:
    }
    '''
    pid = int(url[33:])  # get pid
    post_data = {
        "pid": pid,
        "type": "post",
    }

    with requests.post(POST_URL, headers=HEADERS, data=json.dumps(post_data), timeout=20) as rep:
        if rep.status_code == 200:
            data = rep.json()

            # 下面处理很乱，主要对着返回数据看就很简单
            id = data.get('data').get('post').get('imgs')[0].get('id')
            if id:
                play_url = data.get('data').get('post').get('videos').get(str(id)).get('url')
                if not play_url:
                    play_url = ""
            else:
                play_url = ""
            # --------------------------------------------------------------
        else:
            play_url = ""

    return {
        "play_url": play_url,
    }


if __name__ == "__main__":
    print(get(input("url: ")))