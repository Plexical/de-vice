import re
import hashlib

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

class Analyzer(object):

    basedata = {
        'type': 'unknown',
        'width': 240,
        'height': 320,
        'complete': False,
        'engine': 'unknown'
        }

    def __init__(self, cache):
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

    def query(self, ua):
        return {'complete': True}
