# Python program raising
# exceptions in a python
# thread

import threading
import ctypes
import time


class ThreadWithException(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        # target function of the thread class
        try:
            while True:
                print('running ' + self.name)
        finally:
            print('ended')

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


"""
When we run the code above in a machine and you will notice, as soon as the function raise_exception() is called, 
the target function run() ends. This is because as soon as an exception is raised, program control jumps out of the 
try block and run() function is terminated. After that join() function can be called to kill the thread. 
In the absence of the function run_exception(), the target function run() keeps running forever and join() function 
is never called to kill the thread.
"""
if __name__ == '__main__':
    t1 = ThreadWithException('Thread 1')
    t1.start()
    time.sleep(2)
    t1.raise_exception()
    t1.join()
