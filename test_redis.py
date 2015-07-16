import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')

foo = r.get('foo')

print(foo)
# b'bar'