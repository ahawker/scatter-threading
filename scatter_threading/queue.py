"""
    scatter_threading.queue
    ~~~~~~~~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('ThreadQueueService',)


import Queue as queue
import time

from scatter.exceptions import ScatterTimeout
from scatter.ext.async.queue import Queue, QueueService


class ThreadQueue(Queue):
    """
    """
    queue_cls = queue.Queue

    def join(self, timeout=None):
        """
        """
        if timeout is None:
            return self._queue.join()

        with self._queue.all_tasks_done:
            end = time.time() + timeout
            while self._queue.unfinished_tasks:
                remaining = end - time.time()
                if remaining <= 0:
                    raise ScatterTimeout
                self._queue.all_tasks_done.wait(remaining)


class ThreadQueueService(QueueService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.queue_class = ThreadQueue
        self.queue_max_size = None
        self.queue_empty_exception = queue.Empty
        self.queue_full_exception = queue.Full