# encoding:utf-8

import redis
import webbrowser


r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('foo', 'bar')
foo = r.get('foo')

r.sadd('collection','abc')
r.sadd('collection','def')
r.sadd('collection','fhi')
r.sadd('collection','xwy')

r.zadd('rank',1,'Alibaba')
r.zadd('rank',2,'Tencent')
r.zadd('rank',3,'Baidu')
r.zadd('rank',baidu=3,cc=3,ccc=34)
r.zadd('rank',4,6)

r.rpush('list','www.tantengvip.com')
r.rpush('list','www.qq.com')
r.rpush('list','www.tencent.com')

pop = r.lpop('list')
print(pop)

webbrowser.open('http://www.tantengvip.com',1)
