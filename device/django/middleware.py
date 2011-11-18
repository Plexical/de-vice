import os

from django.conf import settings

path = lambda *s: os.path.abspath(os.path.join(settings.DE_VICE_CACHE, *s))

class DeViceMiddleware(object):

    def process_response(self, request, response):
        return response
