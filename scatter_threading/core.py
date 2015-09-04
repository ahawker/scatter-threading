"""
    scatter_threading.core
    ~~~~~~~~~~~~~~~~~~~~~~

    Asynchronous primitives for threading.
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('Event', 'Condition', 'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Queue', 'Signal')


import Queue as queue
import signal
import threading

from scatter.ext.async import spin_wait


class ScatterThreadEvent(threading._Event):
    """

    """

    def wait(self, timeout=None):
        wait = super(ScatterThreadEvent, self).wait
        return spin_wait(wait, timeout, lambda r: bool(r))


Event = ScatterThreadEvent
Condition = threading.Condition
Lock = threading.Lock
RLock = threading.RLock
Semaphore = threading.Semaphore
BoundedSemaphore = threading.BoundedSemaphore
Queue = queue.Queue
Signal = signal.signal