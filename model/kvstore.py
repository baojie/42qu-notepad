#coding:utf-8

CACHE_DICT = {}

class InterCache(object):
    def __init__(self, cache_dict):
        self.cache = cache_dict

    def get(self, k):
        return self.cache.get(k)

    def set(self, k, v):
        self.cache[k] = v

cache = InterCache(CACHE_DICT)

def kv():
    return cache

if __name__ == "__main__":
    pass
