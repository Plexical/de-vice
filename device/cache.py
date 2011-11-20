import os
import hashlib
import cPickle
from contextlib import closing

class DummyCache(dict):
    """
    A stupid kind of cache: cache directly to memory. Mostly
    intended for testing.
    """

    "Retrieves data by key"
    retreive = lambda s, k: s.get(k, None)

    def store(self, key, data):
        "Cache data by key"
        self[key] = data

class FileCache(object):
    """
    Stores cached items in the file system. A hashing function is used
    on the key to avoid filename limits to affect keys.
    """

    def __init__(self, basepath):
        self.basepath = basepath

    def path(self, key):
        return os.path.join(self.basepath, hashlib.md5(key).hexdigest())

    def retreive(self, key, ):
        "Retreives data by key"
        try:
            with(closing(open(self.path(key), 'rb'))) as fp:
                return cPickle.load(fp)
        except IOError:
            return None

    def store(self, key, data):
        "Cache data by key"
        with(closing(open(self.path(key), 'wb'))) as fp:
            cPickle.dump(data, fp)
