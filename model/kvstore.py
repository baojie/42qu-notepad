#coding:utf-8
import shelve


class KvStorage(object):
    def __init__(self, path):
        db = shelve.open(path)
        self.db = db

    def get(self, k):
        return self.db.get(k)
    
    def get_multi(self, keys):
        result = {}
        for i in keys:
            result[i] = self.get(i)
        return result        

    def set(self, k, v):
        self.db[k] = v
        self.db.sync()


kv = KvStorage('/tmp/42qu.db')

if __name__ == "__main__":
    pass
