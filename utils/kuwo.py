# mp3 url http://www.kuwo.cn/url?format=mp3&rid=65265710&response=url&type=convert_url3&br=320kmp3&from=web


# 320 192 128


# song_info url http://www.kuwo.cn/api/www/music/musicInfo?mid=65265710&reqId=c003efa0-39c7-11ea-a8ad-fdbf6e80b7ac


import requests


HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1516764754.1579334008; _gid=GA1.2.8717020.1579334008; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1579334010; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1579334010; kw_token=MJ3PBY3HDNP',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/play_detail/65265710',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
}


def get(url: str) -> dict:
    '''
    return {
        author:
        song_name:
        play_url:
    }
    '''

    ERROR = {'author': '', 'song_name': '', 'play_url': ''}

    # http://www.kuwo.cn/play_detail/65265710
    id = url[31:][0]

    song_info_url = 'http://www.kuwo.cn/api/www/music/musicInfo?mid={id}'
    mp3_url = 'http://www.kuwo.cn/url?format=mp3&rid={id}&response=url&type=convert_url3&br={quality}&from=web'

    # 得到最高品质以及歌曲信息
    with requests.get(song_info_url.format(id=id), headers=HEADERS, timeout=33) as rep:
        if rep.status_code == 200:
            print(rep.json())
            best_quality = rep.json().get('data').get('songinfo').get('coopFormats')[-1]
            author = rep.json().get('data').get('songinfo').get('artist')
            song_name = rep.json().get('data').get('songinfo').get('songName')
        else:
            return ERROR

    if not best_quality: best_quality = '128kmp3'

    # 得到歌曲链接
    with requests.get(mp3_url.format(id=id, quality=best_quality)) as rep:
        if rep.status_code == 200:
            play_url = rep.json().get('url', '')
        else:
            return ERROR

    return {
        'author': author,
        'song_name': song_name,
        'play_url': play_url,
    }


if __name__ == "__main__":
    print(get(input("url: ")))