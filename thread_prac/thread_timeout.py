import random
import os
import signal
from functools import wraps
from threading import Thread


def search_keyword():
    limit = 20
    cur = 1

    while cur < limit:
        search_page = get_page('www.baidu.com/{}'.format(str(cur)))
        print('cur:', cur)
        if not search_page:
            return
        cur += 1


def get_page(url):
    page = url.split('/')[1]
    print('start page:', url)
    if page % 2 == 0:
        os.kill(os.getppid(), signal.SIGTERM)
    print('end page:', url)
    return ''


def timeout(seconds):
    def crawl_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    return crawl_decorator


class KThread(Thread):
    def __init__(self, *args, **kwargs):
        super(KThread, self).__init__(*args, **kwargs)
        self.killed=False

    def start(self):
        pass

