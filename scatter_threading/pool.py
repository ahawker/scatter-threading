"""
    scatter_threading.pool
    ~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = ('ThreadPoolService',)


from scatter.ext.async.pool import PoolService
from scatter_threading.worker import ThreadWorkerService


class ThreadPoolService(PoolService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.pool_worker_class = ThreadWorkerService