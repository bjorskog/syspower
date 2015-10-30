#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_syspower
----------------------------------

Tests for `syspower` module.
"""

import unittest

from syspower import syspower


class TestSyspower(unittest.TestCase):

    def setUp(self):
        self.client = syspower.Client()

    def tearDown(self):
        pass

    def test_get_series(self):
        data = self.client.get_series("SPOT", "d", "d", "hour")
        print data

    def test_get_series_no_timestamp(self):
        data = self.client.get_series("SPOT", "d", "d", "hour", False)
        print data

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
