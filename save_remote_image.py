# -*- coding: utf-8 -*-

# 使用requests保存远程图片(或文件)
import requests
import os


def saveRemoteImage():
    imgurl = 'http://www.tantengvip.com/wp-content/uploads/2015/01/cropped-13887362_13887362_1347773771848.jpg'
    filename = imgurl.split('/')[-1]
    path = './static/'+filename
    if not os.path.exists(path):
        r = requests.get(imgurl)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('OK')
    else:
        print('Already exists.')

    """
    下载大文件这样写：
    for chunk in r.iter_content():
        f.write(chunk)

    如果不使用requests模块：
    import urllib
    urllib.urlretrieve(url, filename=None, reporthook=None, data=None)
    """

saveRemoteImage()
