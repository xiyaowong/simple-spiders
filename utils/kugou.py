import re

import requests

HEADERS = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'referer':
    'https://www.kugou.com/song/',
    'cookie':
    'kg_mid=f679eeece44cf6bec74d2867be4901f7; kg_dfid=2kuKRO3GStCZ0VBY9V12pXeT; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1574177549,1576216623,1576386693; kg_mid_temp=f679eeece44cf6bec74d2867be4901f7; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1576387198',
}

GET_SONG_INFO_URL = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={hash}"

HASH_PATTERN = r'"hash":"(.*?)",'

def get(url):
    '''
    return {
        author_name:
        song_name:
        play_url:
        img:
    }
    '''
    ERROR = {
        'author_name': '',
        'song_name': '',
        'play_url': '',
        'img': '',
    }

    # get hash
    with requests.get(url, headers=HEADERS, timeout=50) as rep:
        if rep.status_code == 200:
            hash = re.findall(HASH_PATTERN, rep.text)[0]
        else:
            return ERROR

    # get song info
    with requests.get(GET_SONG_INFO_URL.format(hash=hash), headers=HEADERS, timeout=50) as rep:
        if rep.status_code == 200:
            if rep.json().get('status') == 1: # 这里的判断其实没什么必要，是酷狗接口自带的
                data = rep.json().get('data')
                author_name = data.get('author_name', '')
                song_name = data.get('song_name', '')
                play_url = data.get('play_url', '')
                img = data.get('img', '')
                return {
                    'author_name': author_name,
                    'song_name': song_name,
                    'play_url': play_url,
                    'img': img,
                }
            else:
                return ERROR
        else:
            return ERROR


if __name__ == "__main__":
    print(get(input('url: ')))