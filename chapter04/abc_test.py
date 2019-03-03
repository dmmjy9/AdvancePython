# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#     def set(self, key, value):
#         raise NotImplementedError
#
# class RedisCache(CacheBase):
#     pass

import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    @abc.abstractmethod
    def set(self, key, value):
        pass
class RedisCache(CacheBase):
    def get(self, key):
        print(key)
    def set(self, key, value):
        print("SET: {x} {y}".format(x=key, y=value))
redis_cache = RedisCache()
redis_cache.set("key", "value")
