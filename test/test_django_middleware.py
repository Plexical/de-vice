import py
import imp
import sys
import os

try:
    import django
    import django_pytest
except ImportError:
    py.test.skip("This test test needs Django and django-pytest to run")

from django.conf import settings

from device.django.middleware import *

from contextlib import contextmanager

@contextmanager
def patched_settings(**custom):
    changed = {}
    for key, val in custom.iteritems():
        changed[key] = getattr(settings, key, None)
        setattr(settings, key, val)
    yield
    for key, old in changed.iteritems():
        if old is None:
            delattr(settings, key)
        else:
            setattr(settings, key, old)

def setup_module(mod):
    mod.fake_settings = imp.new_module('de_vice_fake_settings')
    sys.modules['de_vice_fake_settings'] = mod.fake_settings
    mod.old_dj_settings = os.environ.get('DJANGO_SETTINGS_MODULE', None)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'de_vice_fake_settings'

def teardown_module(mod):
    if mod.old_dj_settings is not None:
        os.environ['DJANGO_SETTINGS_MODULE'] = mod.old_dj_settings
    else:
        del os.environ['DJANGO_SETTINGS_MODULE']
    del sys.modules['de_vice_fake_settings']

def test_path():
    with(patched_settings(DE_VICE_CACHE='/tmp')):
        assert path('foo') == '/tmp/foo'
