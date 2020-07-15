# Python program using
# traces to kill threads

import sys
import threading
import time


"""
This methods works by installing traces in each thread. Each trace terminates itself on the detection of
 some stimulus or flag, thus instantly killing the associated thread. For Example

In this code, start() is slightly modified to set the system trace function using settrace(). 
The local trace function is defined such that, whenever the kill flag (killed) of the respective thread is set,
 a SystemExit exception is raised upon the excution of the next line of code,
  which end the execution of the target function func. Now the thread can be killed with join().
"""


class ThreadWithTrace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True


def func():
    while True:
        print('thread running')


t1 = ThreadWithTrace(target=func)
t1.start()
time.sleep(2)
t1.kill()
t1.join()
if not t1.isAlive():
    print('thread killed')
