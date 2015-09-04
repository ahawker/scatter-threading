"""
    scatter_threading.service
    ~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('ThreadAsyncService',)


from scatter.ext.async import AsyncService
from scatter_threading.future import ThreadFutureService
from scatter_threading.pool import ThreadPoolService
from scatter_threading.queue import ThreadQueueService


class ThreadAsyncService(AsyncService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """

        """
        self.response_queue_class = ThreadQueueService
        self.worker_pool_class = ThreadPoolService
        self.futures_class = ThreadFutureService