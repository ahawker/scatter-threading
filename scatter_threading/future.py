"""
    scatter_threading.future
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = ('ThreadFuture', 'ThreadFutureService')


from scatter.ext.async.future import Future, FutureService, ScatterFuture
from scatter_threading.core import Event, RLock


class ThreadScatterFuture(ScatterFuture):
    """

    """

    lock_cls = RLock

    event_cls = Event


class ThreadFuture(Future):
    """

    """

    future_cls = ThreadScatterFuture


class ThreadFutureService(FutureService):
    """

    """

    def on_initializing(self, *args, **kwargs):
        """

        """
        self.future_class = ThreadFuture