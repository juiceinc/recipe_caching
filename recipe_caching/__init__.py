# -*- coding: utf-8 -*-
"""
Recipe
~~~~~~~~~~~~~~~~~~~~~
"""
import functools
import logging

from recipe_caching.caching_query import CachingQuery

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:

    class NullHandler(logging.Handler):

        def emit(self, record):
            pass


logging.getLogger(__name__).addHandler(NullHandler())


def query_callable(regions, query_cls=CachingQuery):
    return functools.partial(query_cls, regions)


__all__ = [query_callable]
