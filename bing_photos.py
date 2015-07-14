#!/usr/bin/env python

# -*- coding:utf-8 -*-

# -*- author:arron ni-*-

# python3抓取bing主页所有背景图片

import urllib.request
import re
import sys
import os


def get_bing_backphoto():
    if os.path.exists('photos') == False:
        os.mkdir('photos')

    for i in range(0, 30):

        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=' + str(i) + '&n=1&nc=1361089515117&FORM=HYLH1'

        html = urllib.request.urlopen(url).read()

        if html == 'null':
            print('open & read bing error!')

            sys.exit(-1)

        html = html.decode('utf-8')

        reg = re.compile('"url":"(.*?)","urlbase"', re.S)

        text = re.findall(reg, html)

        # http://s.cn.bing.net/az/hprichbg/rb/LongJi_ZH-CN8658435963_1366x768.jpg

        for imgurl in text:
            right = imgurl.rindex('/')

            name = imgurl.replace(imgurl[:right + 1], '')

            savepath = 'photos/' + name

            urllib.request.urlretrieve(imgurl, savepath)

            print(name + ' save success!')


get_bing_backphoto()