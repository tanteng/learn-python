# -*- coding:utf-8 -*-

from pymongo import MongoClient
import time
import re
import os
import gridfs
import sys

client = MongoClient('mongodb://192.168.6.212:27017/send_excel')
db = client.js_send_excel
fs = gridfs.GridFS(db)

files = fs.find()

time_start = time.clock()
print('总数：', files.count())
count = 0

for ffle in files:
    filename = ffle.filename

    m = re.match(r'发货订单', filename)

    if m and filename.find('xls') > 0 and not os.path.isfile('./excel/' + filename):
        with open('./excel2/' + filename, 'wb') as f1:
            f1.write(ffle.read())
            count += 1

print('执行时间{0}秒'.format(time.clock() - time_start))
print('本次更新{0}个文档'.format(count))
