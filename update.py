import time

import memcache

import settings
from lib.scores import BingSearcher


mc = memcache.Client(['127.0.0.1:11211'])

while (True):
    bing_searcher = BingSearcher(settings.BING_ID)
    scores = bing_searcher.get_scores('happy', 'sad')
    mc.set_multi(scores)
    time.sleep(settings.UPDATE_INTERVAL)
