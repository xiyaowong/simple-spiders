from urllib.parse import urlparse

import requests as rs


def get(url: str) -> dict:
    """
    Args:
        url: example(https://lizhi.fm/vod/*****/**********)
    Returns:
        {
            userName: ""
            voiceName: ""
            voiceUrl: ""
        }

    """
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"}
    info_url = "https://m.lizhi.fm/vodapi/voice/info/{id}"

    path = urlparse(url).path
    voiceId = path.split("/")[-1]
    if voiceId:
        rep = rs.get(info_url.format(id=voiceId), headers=headers)
        if rep.status_code == 200:
            info = rep.json()
            if info['code'] == 0:
                userName = info.get("data").get("userVoice").get("userInfo").get("name")
                voiceName = info.get("data").get("userVoice").get("voiceInfo").get("name")
                voiceUrl= info.get("data").get("userVoice").get("voicePlayProperty").get("trackUrl")
            else:
                userName = ""
                voiceName = ""
                voiceUrl = ""
        else:
            userName = ""
            voiceName = ""
            voiceUrl = ""
    else:
        userName = ""
        voiceName = ""
        voiceUrl = ""


    return {
        "userName": userName,
        "voiceName": voiceName,
        "voiceUrl": voiceUrl,
    }


if __name__ == "__main__":
    url = input("url: ")
    print(get(url))