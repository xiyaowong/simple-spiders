import os
import requests


class KuGou:
    def __init__(self):
        self.headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
            'referer':
            'https://www.kugou.com/song/',
            'cookie':
            'kg_mid=f679eeece44cf6bec74d2867be4901f7; kg_dfid=2kuKRO3GStCZ0VBY9V12pXeT; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1574177549,1576216623,1576386693; kg_mid_temp=f679eeece44cf6bec74d2867be4901f7; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1576387198',
        }
        self.search_url = 'https://songsearch.kugou.com/song_search_v2?keyword={kw}&page=1&pagesize=50&platform=WebFilter&filter=2&iscorrection=1'
        self.get_song_info_url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={hash}'

    def search(self, kw: str):
        '''
        data: [
            {
                singer_name:
                song_name:
                file_name:
                hash:
            },
        ]
        '''

        data = []
        with requests.get(self.search_url.format(kw=kw), headers=self.headers) as rep:
            if rep.status_code == 200:
                data_lists = rep.json().get('data').get('lists')
                for data_list in data_lists:
                    data.append(
                        {
                            'singer_name': data_list['SingerName'],
                            'song_name': data_list['SongName'],
                            'file_name': data_list['FileName'],
                            'hash': data_list['FileHash'],
                        }
                    )
                return data
            else:
                return None

    def _get_song_info(self, hash):
        with requests.get(self.get_song_info_url.format(hash=hash), headers=self.headers) as rep:
            if rep.status_code == 200:
                data = rep.json().get('data')
                song_info = {
                    'audio_name': data['audio_name'],
                    'lyrics': data['lyrics'],
                    'play_url': data['play_url'],
                    'img': data['img'],
                }
                return song_info
            else:
                return None

    def download(self, hash):
        song_info = self._get_song_info(hash)
        file_name = song_info['audio_name']
        file_url = song_info['play_url']

        if not os.path.exists('kugou'):
            os.mkdir('kugou')

        print(f'*********\n正在下载歌曲"{file_name}"')
        with requests.get(file_url, headers=self.headers) as rep:
            with open(f'kugou/{file_name}.mp3', 'wb') as file:
                file.write(rep.content)
                print("下载完成\n*************")


def main():
    kugou = KuGou()
    while True:
        print("你可以随时输入'q'来退出应用！\n-------------------------------")
        try:
            kw = input("请输入你想搜索的歌曲关键字：")
            if kw == 'q':
                break
            search_result = kugou.search(kw)
            print("搜索结果：")
            print("id  | 歌曲名")
            print("-"*16)
            for i in range(len(search_result)):
                print('{:<4}| {}'.format(i+1, search_result[i]['file_name']))
            select_id = input("请输入上方你想下载的歌曲对应的id：")
            if select_id == 'q':
                break
            select_id = int(select_id)
            select_song = search_result[select_id - 1]
            song_hash = select_song['hash']
            kugou.download(song_hash)
        except:
            print("请保证输入内容有效！当然也有可能是程序除了问题\n-------------------------------------")


if __name__ == "__main__":
    main()




