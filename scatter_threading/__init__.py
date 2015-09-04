"""
    scatter-threading
    ~~~~~~~~~~~~~~~~~~~~~~

    Package which contains extensions of `scatter-async` for using the
    python standard library `threading` module.

    :copyright: (c) 2014 Andrew Hawker.
    :license: ?, See LICENSE file.
"""

ENABLED = True

import itertools

from scatter_threading import core
from scatter_threading.core import *
from scatter_threading import future
from scatter_threading.future import *
from scatter_threading import pool
from scatter_threading.pool import *
from scatter_threading import queue
from scatter_threading.queue import *
from scatter_threading import service
from scatter_threading.service import *
from scatter_threading import worker
from scatter_threading.worker import *


__all__ = list(itertools.chain(core.__all__,
                               future.__all__,
                               pool.__all__,
                               queue.__all__,
                               service.__all__,
                               worker.__all__))
