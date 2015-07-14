from pymongo import MongoClient
import gridfs
import time
import re
import os
import sys

client = MongoClient('mongodb://192.168.1.22:27017/excel')
db = client.js_send_excel
fs = gridfs.GridFS(db)
files = fs.find()

time_start = time.clock()
print('总数：', files.count())

for ffle in files:
    filename = ffle.filename
    m = re.match(r'发货订单', filename)

    if m and filename.find('.xls') > 0 and not os.path.isfile('./excel/' + filename):
        with open('./excel/' + filename, 'wb') as f1:
            f1.write(ffle.read())

print('执行时间{0}秒'.format(time.clock() - time_start))