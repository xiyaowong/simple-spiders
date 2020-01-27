import bilibili_cover, changya, pipigaoxiao, kuwo, kugou, quanminkge, weishi


def get(t=None, url=''):
    if t and url:
        if t == 'bilibili_cover':
            return bilibili_cover.get(url)
        elif t == 'changya':
            return changya.get(url)
        elif t == 'pipigaoxiao':
            return pipigaoxiao.get(url)
        elif t == 'kuwo':
            return kuwo.get(url)
        elif t == 'kugou':
            return kugou.get(url)
        elif t == 'weishi':
            return weishi.get(url)
        elif t == 'quanminkge':
            return quanminkge.get(url)
        else:
            return {'msg':'missing data! ts can be bilibili_cover, changya, pipigaoxiao, kuwo, kugou, quanminkge, weishi. url is required!'}
    else:
        return {'msg':'missing data! ts can be bilibili_cover, changya, pipigaoxiao, kuwo, kugou, quanminkge, weishi. url is required!'}


if __name__ == "__main__":
    a = get(t='bilibili_cover', url='https://www.bilibili.com/video/av78977736')
    print(a)