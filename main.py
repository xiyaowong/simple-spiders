from enum import Enum

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from pydantic import BaseModel

from platforms import *

app = FastAPI()

class Platform(str, Enum):
    bilibili = "bilibili"
    changya = "changya"
    douyin = "douyin"
    kugou = "kugou"
    kuwo = "kuwo"
    lizhiFM = "lizhiFM"
    pipigaoxiao = "pipigaoxiao"
    quanminkge = "quanminkge"
    weibo = "weibo"
    weishi = "weishi"
    zhihu_video = "zhihu_video"
    zuiyou_voice = "zuiyou_voice"


@app.get("/", response_class=HTMLResponse)
def hello():
    return HTMLResponse("go path docs")

@app.get("/{platform}/")
def extract(platform: Platform, url: str):
    """
    ## 各项返回值如下：
    * bilibili(哔哩哔哩视频封面和视频):
        * cover_url: ""
        * video_url: ""
    * changya(唱鸭音频):
        * author: ""
        * audio_name: ""
        * audio_url: ""
    * douyin(逗音无水印):
        * video_name: ""
        * video_url: ""
    * kugou(酷狗单曲):
        * author_name: ""
        * song_name: ""
        * play_url: ""
        * img: ""
    * kuwo(酷我单曲):
        * author: ""
        * song_name: ""
        * play_url: ""
    * lizhiFM(荔枝FM音频):
        * userName: ""
        * voiceName: ""
        * voiceUrl: ""
    * pipigaoxiao(皮皮搞笑无水印):
        * play_url: ""
    * quanminkge(全民k歌音频及mv):
        * singer: ""
        * song_name: ""
        * play_url: ""
        * play_video: ""
    * weibo(微博视频):
        * title:
        * urls:{
            * mp4_720p_mp4: ""
            * mp4_hd_mp4: ""
            * mp4_ld_mp4: ""}
    * weishi(微视无水印视频):
        * title: ""
        * play_url: ""
    * zhihu_video(知乎视频):
        * urls: []
    * zuiyou_voice(最右语音评论音频):
        * voice_text: ""
        * uri: ""
        * org_uri: ""
    """
    return eval(platform.value).get(url)
