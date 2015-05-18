"""
Tests for cache_utils.py
"""
from mock import MagicMock
from unittest import TestCase

from openedx.core.lib.cache_utils import memoize_in_request_cache


class TestMemoizeInRequestCache(TestCase):
    """
    Test the memoize_in_request_cache helper function.
    """
    class TestCache(object):
        """
        A test cache that provides a data dict for caching values, analogous to the request_cache.
        """
        data = {}

    def setUp(self):
        super(TestMemoizeInRequestCache, self).setUp()
        self.request_cache = self.TestCache()

    @memoize_in_request_cache('request_cache')
    def func_to_memoize(self, param):
        """
        A test function whose results are to be memoized in the request_cache.
        """
        return self.func_to_count(param)

    def test_memoize_in_request_cache(self):
        self.func_to_count = MagicMock()  # pylint: disable=attribute-defined-outside-init
        self.assertFalse(self.func_to_count.called)

        self.func_to_memoize('foo')
        self.func_to_count.assert_called_once_with('foo')

        self.func_to_memoize('foo')
        self.func_to_count.assert_called_once_with('foo')

        for _ in range(10):
            self.func_to_memoize('foo')
            self.func_to_memoize('bar')

        self.assertEquals(self.func_to_count.call_count, 2)
