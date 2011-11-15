import sys
import re
import hashlib
import json

import requests

from cache import DummyCache

digest = lambda ua: hashlib.md5(ua).hexdigest()

def rule(matches, **changes):
    return dict(re=re.compile(matches),
                m=matches, # XXX dev
                changes=changes)

partial_matchers = (
    rule('Macintosh|Windows|Linux|BSD|SunOS|DragonFly|Mac_PowerPC',
         type='desktop'),
    rule('Mobile Safari', type='mobile'),
    rule('Gecko\/', engine='gecko'),
    rule('Firefox', complete=True, svg=True, app='firefox'),
    rule('MSIE', engine='trident'),
    rule('KHTML\/', engine='khtml'),
    rule('Safari', engine='webkit', app='safari'),
    rule('Chrome', engine='webkit', app='chrome'),
    rule('Opera', engine='presto'),
    rule('iPhone|iPod', type='mobile', complete=True, width=320, height=480,
         svg=True),
    rule('iPad', type='mobile', complete=True, width=1024, height=768,
         svg=True)
    )

def uaencode(ua):
    return ua.replace(' ', '_').replace(';', '*')

class DummyCache(dict):
    retreive = lambda s, k: s.get(k, None)

    def store(self, key, data):
        self[key] = data

class WebServiceFailed(Exception): pass

class Analyzer(object):

    basedata = {
        'type': 'unknown',
        'width': 240,
        'height': 320,
        'complete': False,
        'engine': 'unknown'
        }

    def __init__(self, cache=None):
        if cache is None:
            cache = DummyCache()
        self.cache = cache

    def analyze(self, ua):
        hashed = digest(ua)
        info = self.cache.retreive(hashed)
        if info:
            return info
        else:
            info = self.calculate(hashed, ua)
            self.cache.store(hashed, info)
            return info

    def calculate(self, hashed, ua):
        info = self.basedata.copy()
        info['digest'] = hashed
        for pm in partial_matchers:
            if pm['re'].search(ua):
                info.update(pm['changes'])
                if pm.get('complete', False):
                    break

        # XXX stopgap measure
        if info.get('type', False) == 'desktop' and not info['complete']:
            info['complete'] = True

        if not info['complete']:
            info.update(self.query(ua))

        return info

    def _webservice(self, ua):
        res = requests.get('http://cgi.plexical.com/dimensions.py',
                           params={'ua': ua})
        if res.ok:
            return json.loads(res.content)
        else:
            raise WebserviceFailed(("Plexical WURFL web service failed with "
                                    "status code %d" % status_code))

    def query(self, ua):
        struct = self._webservice(uaencode(ua))
        return {'complete': True,
                'width': struct['resolution_width'],
                'height': struct['resolution_height']}

if __name__ == '__main__':
    analyzer = Analyzer()
    print(json.dumps(analyzer.analyze(sys.argv[1])))
