"""
    scatter_threading.worker
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = ('ThreadWorkerService',)


import Queue as queue
import sys
import threading

from scatter.ext.async import spin_wait, Worker, WorkerService
from scatter.exceptions import ScatterExit
from scatter_threading.core import Event
from scatter_threading.queue import ThreadQueue


class ScatterThread(threading.Thread):
    """

    """

    def __init__(self, func, *args, **kwargs):
        super(ScatterThread, self).__init__(target=func, args=args, kwargs=kwargs)
        self.daemon = True
        self._seconds = 0
        self._started = Event()
        self._completed = Event()
        self._cancelled = Event()

    @property
    def id(self):
        return self.ident

    def start_later(self, seconds):
        """
        """
        self._seconds = seconds
        self.start()

    def started(self):
        """
        """
        return self._started.is_set()

    def running(self):
        """
        """
        return self.is_alive()

    def completed(self):
        """
        """
        return self._completed.is_set()

    def wait_for_start(self, timeout=None):
        """
        """
        return self._started.wait(timeout)

    def wait_for_completion(self, timeout=None):
        """
        """
        return self._completed.wait(timeout)

    def run(self):
        """
        """
        cancelled = self._cancelled.wait(self._seconds)
        if cancelled:
            return

        self._started.set()
        try:
            super(ScatterThread, self).run()
        finally:
            self._completed.set()

    def cancel(self):
        """
        """
        self._cancelled.set()
        return not self.started()

    def stop(self, exception=ScatterExit, block=True, timeout=None):
        """
        """
        try:
            import ctypes
        except ImportError:
            return False
        else:
            exc = ctypes.py_object(exception)
            ident = ctypes.c_long(self.ident)
            result = ctypes.pythonapi.PyThreadState_SetAsyncExc(ident, exc)

            # Invalid thread id (?).
            if result == 0:
                return False

            # Error code; revert and fail.
            if result != 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(ident, None)
                return False

            return self.join(timeout) if block else True

    def join(self, timeout=None):
        join = super(ScatterThread, self).join
        return spin_wait(join, timeout, lambda r: not self.is_alive())

    def get(self, block=True, timeout=None):
        """
        """
        return self._result.get(block, timeout)

    def is_current(self):
        """
        """
        return threading.current_thread() is self


class ThreadWorker(Worker):
    """
    """

    worker_cls = ScatterThread


class ThreadWorkerService(WorkerService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.worker_class = ThreadWorker