"""
提取新浪微博视频：
Function:
    get(url:  str):
        return {
            'title': title or '',
            'urls':{
                'mp4_720p_mp4': mp4_720p_mp4 or '',
                'mp4_hd_mp4': mp4_hd_mp4 or '',
                'mp4_ld_mp4': mp4_ld_mp4 or '',
            }
        }
------------
    url example:
        https://weibo.com/3929428825/IuXpilm1p（pc）
        https://m.weibo.cn/5658716867/4474073062821340（mobile）
"""
import re
import requests


def get(url: str) -> dict:
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}
    title_re = r'"title": "(.*?)",'
    mp4_720p_mp4_re = r'"mp4_720p_mp4": "(.*?)",'
    mp4_hd_mp4_re = r'"mp4_hd_mp4": "(.*?)",'
    mp4_ld_mp4_re = r'"mp4_ld_mp4": "(.*?)"'

    rep = requests.get(url, headers=headers, timeout=20)
    if rep.status_code == 200:
        text = rep.text

        try:
            title = re.findall(title_re, text)[0]
        except IndexError:
            title = ''

        try:
            mp4_720p_mp4 = re.findall(mp4_720p_mp4_re, text)[0]
        except IndexError:
            mp4_720p_mp4 = ''

        try:
            mp4_hd_mp4 = re.findall(mp4_hd_mp4_re, text)[0]
        except IndexError:
            mp4_hd_mp4 = ''

        try:
            mp4_ld_mp4 = re.findall(mp4_ld_mp4_re, text)[0]
        except IndexError:
            mp4_ld_mp4 = ''

    return {
        'title': title or '',
        'urls':{
            'mp4_720p_mp4': mp4_720p_mp4 or '',
            'mp4_hd_mp4': mp4_hd_mp4 or '',
            'mp4_ld_mp4': mp4_ld_mp4 or '',
        }
    }


if __name__ == "__main__":
    # url = 'https://m.weibo.cn/5658716867/4474073062821340'
    # url = 'https://weibo.com/3929428825/IuXpilm1p?type=comment'
    url = input('url: ')
    print(get(url))