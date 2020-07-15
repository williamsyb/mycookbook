# Python program killing
# a thread using multiprocessing
# module

"""
Though the interface of the two modules is similar, the two modules have very different implementations.
All the threads share global variables, whereas processes are completely separate from each other.
Hence, killing processes is much safer as compared to killing threads. The Process class is provided a method,
terminate(), to kill a process. Now, getting back to the initial problem. Suppose in the above code,
we want to kill all the processes after 0.03s have passed.
This functionality is achieved using the multiprocessing module in the following code.
"""
import multiprocessing
import time


def func(number):
    for i in range(1, 10):
        time.sleep(0.01)
        print('Processing ' + str(number) + ': prints ' + str(number * i))

    # list of all processes, so that they can be killed afterwards


all_processes = []

for i in range(0, 3):
    process = multiprocessing.Process(target=func, args=(i,))
    process.start()
    all_processes.append(process)

# kill all processes after 0.03s
time.sleep(0.03)
for process in all_processes:
    process.terminate()
