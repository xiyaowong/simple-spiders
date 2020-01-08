import re
import json
import requests

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
}
audio_pattern = r'<audio src="(http://cdn.singroom.i52hz.com/.*?)" preload="metadata"'
author_pattern = r'"nickname":"(.*?)",'
song_pattern = r'"songName":"(.*?)",'
# download changya audio
def get(url):
    try:
        rep = requests.get(url, headers=HEADERS, timeout=30)
        if rep.status_code == 200:
            html = rep.text
            audio_url = re.findall(audio_pattern, html)[0]
            author = re.findall(author_pattern, html)[0]
            song = re.findall(song_pattern, html)[0]

            with requests.get(audio_url, headers=HEADERS) as rep:
                if rep.status_code == 200:
                    print(f'正在下载《{author}-{song}.mp3》，稍等。。。')
                    with open(f'{author}-{song}.mp3', 'wb') as file:
                        file.write(rep.content)
                        print(f'《{author}-{song}.mp3》下载完成!')
                        return True
        else:
            print('出现问题，请再尝试，多次不行就别用了！')
            return False
    except:
        print("发生了一点问题，请确保链接输入正确，网络没问题！")


if __name__ == "__main__":
    while True:
        url = input("请输入“唱鸭”歌曲分享链接： ")
        if get(url):
            break
