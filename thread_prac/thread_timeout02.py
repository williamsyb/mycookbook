import sys

import signal
import functools


class TimeoutError(Exception):
    pass


def timeout(seconds, error_message="Timeout Error: the cmd 30s have not finished."):
    def decorated(func):
        result = ""

        def _handle_timeout(signum, frame):
            global result
            result = error_message
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            global result
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                return result
            return result

        return functools.wraps(func)(wrapper)

    return decorated


@timeout(5)  # 限定下面的slowfunc函数如果在5s内不返回就强制抛TimeoutError Exception结束
def slowfunc(sleep_time):
    a = 1
    import time
    time.sleep(sleep_time)
    return a


# slowfunc(3) #sleep 3秒，正常返回 没有异常


print(slowfunc(11))  # 被终止