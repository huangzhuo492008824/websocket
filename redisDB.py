import redis


class RedisDB(object):
    """Simple Queue with Redis Backend"""
    def __init__(self, namespace='websocket', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db = redis.StrictRedis.from_url(url='redis://localhost:6379/0')
        self.key = '%s:' % namespace

    def set(self, key, val, ex=None):
        self.__db.set(self.key+key, val, ex=ex)

    def get(self, key):
        return self.__db.get(self.key+key)

    def delete(self, key):
        return self.__db.delete(self.key+key)