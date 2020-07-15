
# Python program killing
# a thread using ._stop()
# function

import time
import threading
"""
Using a hidden function _stop() :
In order to kill a thread, we use hidden function _stop() this function is not documented 
but might disappear in the next version of python.
"""


class MyThread(threading.Thread):

    # Thread class with a _stop() method.
    # The thread itself has to check
    # regularly for the stopped() condition.

    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

        # function using _stop function

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        while True:
            if self.stopped():
                return
            print("Hello, world!")
            time.sleep(1)


t1 = MyThread()

t1.start()
time.sleep(5)
t1.stop()
t1.join()