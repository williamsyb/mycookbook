#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 多线程有用方法模块
# Create: 2008-8-30
# Author: MK2[fengmk2@gmail.com]

import threading, time
import sys

from fileauth.public.utility import exceptionMgr


class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill()
    method.
    
    Come from:
    Kill a thread in Python: 
    http://mail.python.org/pipermail/python-list/2004-May/260937.html
    """

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False
        self.exception = None

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
        trace."""
        sys.settrace(self.globaltrace)
        try:
            self.__run_backup()
        except Exception as e:
            error_detail = exceptionMgr.on_except()
            self.exception = e
            setattr(self.exception, 'error_detail', error_detail)
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True


class Timeout(Exception):
    """function run timeout"""


def timeout(seconds):
    """超时装饰器，指定超时时间
    若被装饰的方法在指定的时间内未返回，则抛出Timeout异常"""

    def timeout_decorator(func):
        """真正的装饰器"""

        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        def _(*args, **kwargs):
            result = []
            # create new args for _new_func, because we want to get the func return val to result list
            new_kwargs = {
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
            }
            thd = KThread(target=_new_func, kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            thd.kill()  # kill the child thread
            if alive:
                raise Timeout(u'function run too long, timeout %d seconds.' % seconds)
            elif thd.exception is not None:
                # print thd.exception.error_detail
                raise thd.exception
            return result[0]

        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _

    return timeout_decorator


@timeout(5)
def method_timeout(seconds, text):
    print('start', seconds, text)
    time.sleep(seconds)
    print('finish', seconds, text)
    return seconds


class TimeoutTester(object):

    def __init__(self, sec):
        self._name = 'time out tester%d' % sec

    @timeout(5)
    def dosomething(self, seconds, text):
        print(self._name, 'start', seconds, text)
        time.sleep(seconds)
        print(self._name, 'finish', seconds, text)
        return seconds


@timeout(5)
def test_exception():
    raise Exception('test timeout')


if __name__ == '__main__':
    try:
        test_exception()
    except Exception as e:
        assert 'test timeout' == str(e)
    for sec in range(3, 10):
        try:
            print('*' * 20)
            print(method_timeout(sec, 'test waiting %d seconds' % sec))
        except Timeout as e:
            print(e)
        try:
            print('*' * 20)
            tester = TimeoutTester(sec)
            tester.dosomething(sec, 'test waiting %d seconds' % sec)
        except Timeout as e:
            print(e)
