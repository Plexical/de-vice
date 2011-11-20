from device.cache import *
import sys
import tempfile
import shutil

from StringIO import StringIO

def test_dummy_cache():
    cache = DummyCache()
    cache.store('foo', 'bar')
    assert cache.retreive('foo') == 'bar'

def test_fs_cache_roundtrip():
    tmpd = tempfile.mkdtemp()
    try:
        cache1 = FileCache(tmpd)
        cache1.store("foo", "bar")
        cache2 = FileCache(tmpd)
        assert cache2.retreive("foo") == "bar"
    finally:
        shutil.rmtree(tmpd)

def test_fs_cache_miss():
    assert FileCache('/no/such/path').retreive('foo') is None
