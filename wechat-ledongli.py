#coding: utf-8

#date: 刷微信步数

#usage: edit steps and ledongli's uid(u need to download this app) .That would be ok .Good luck. ^_^

import requests

import sys

import json

import datetime

import time

def isnum(value):

    try:

        temp = int(value)

    except Exception as e:

        return False

    else:

        return True

# like 2015-09-25 00:00:00 converts to unix time stamp

def formatDate():

    nowtime = datetime.datetime.now()

    date = time.strftime('%Y-%m-%d')

    strtemp_date = date + ' 00:00:00'

    ledongli_date = time.strptime(strtemp_date, '%Y-%m-%d %H:%M:%S')

    finaldate = time.mktime(ledongli_date) # rusult is 1443456000.0(float type), but still need to format to 1443456000

    finaldate = int(finaldate)

    return finaldate

def main(steps, uid):

    if not isnum(steps):

        print('param error. steps must be an integer.')

    url = 'http://pl.api.ledongli.cn/xq/io.ashx'

    fake_headers = {

                        'User-Agent'     : 'le dong li/5.4 (iPhone; iOS 9.1; Scale/2.00)',

                        'Content-Type'   : 'application/x-www-form-urlencoded; charset=UTF-8',

                        'Accept-Encoding': 'gzip'

                    }

    keycontentjson = [

                        {

                            "date": formatDate(),
                            "calories": 0,
                            "activeValue": 108,
                            "steps": steps,
                            "pm2d5": 0,
                            "duration": 0,
                            "distance": 0,
                            "report": "[]"

                        }

                     ]

    # key is a str type

    # key must be a json data convert to string

    key = json.dumps(keycontentjson)

    param = {

                'action': 'profile',

                'pc':     '29e39ed274ea8e7a50f8a83abf1239faca843022',

                'cmd':    'updatedaily',

                'uid':    uid,

                'list':   key,
                 'v'  :   '5.4%20ios',
                 'vc' : '540%20ios'
            }

    r = requests.post(url, data = param, headers = fake_headers)

    print(r.text)

    print('装逼成功')

if __name__ == '__main__':

    steps = 199999

    uid = '1111111'

    main(steps, uid)