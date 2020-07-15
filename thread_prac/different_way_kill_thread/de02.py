# Python program showing
# how to kill threads
# using set/reset stop
# flag

import threading
import time


def run():
    while True:
        print('thread running')
        global stop_threads
        if stop_threads:
            break


"""
Set/Reset stop flag :
In order to kill a threads, we can declare a stop flag and this flag will be check occasionally by the thread.

For Example
In the above code, as soon as the global variable stop_threads is set, the target function run() ends and 
the thread t1 can be killed by using t1.join(). But one may refrain from using global variable due to certain reasons.
For those situations, function objects can be passed to provide a similar functionality as shown below.
"""


def main():
    stop_threads = False
    t1 = threading.Thread(target=run, args=(lambda: stop_threads,))
    t1.start()
    time.sleep(1)
    stop_threads = True
    t1.join()
    print('thread killed')


def run(stop):
    while True:
        print('thread running')
        if stop():
                break


if __name__ == '__main__':
    stop_threads = False
    t1 = threading.Thread(target=run)
    t1.start()
    time.sleep(1)
    stop_threads = True
    t1.join()
    print('thread killed')

    main()
