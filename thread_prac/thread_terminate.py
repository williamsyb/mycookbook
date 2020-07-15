# This code module allows you to kill threads.  The
# class KThread is a drop-in replacement for
# threading.Thread.  It adds the kill() method, which
# should stop most threads in their tracks.
#
# #
# ---------------------------------------------------------------------
# # KThread.py: A killable Thread implementation.
# #
# ---------------------------------------------------------------------

import sys
import threading


class KThread(threading.Thread):
    """
       A subclass of threading.
       Thread, with a kill() method.
    """

    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
    trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
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


# ------------------------------------------------------------------------
# Example usage:
# ------------------------------------------------------------------------

# This illustrates running a function in a separate
# thread.  The thread is
# killed before the function finishes.

# from KThread import *

def func():
    print('Function started')
    for _ in range(1000000):
        pass
    print('Function finished')


A = KThread(target=func)
A.start()
for i in range(1000000):
    pass
A.kill()

print('End of main program')

# Output:
#
#   Function started
#   End of main program
#
#
# -----------------------------------------------------------------------
# How It Works:
# -----------------------------------------------------------------------
#
# The KThread class works by installing a trace in the
# thread.  The trace
# checks at every line of execution whether it should
# terminate itself.
# So it's possible to instantly kill any actively
# executing Python code.
# However, if your code hangs at a lower level than
# Python, then the
# thread will not actually be killed until the next
# Python statement is
# executed.
#
# -----------------------------------------------------------------------
# Considerations:
# -----------------------------------------------------------------------
#
# Certain IDEs may install their own threading trace
# code, for debugging
# purposes.  This module is incompatible with those
# IDEs.
#
# Consider bugging the Python folks, until they give us
# a thread kill
# method.  The code has already been written:
