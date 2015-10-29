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
        pass

    def tearDown(self):
        pass

    def test_client(self):
        client = syspower.Client()
        data = client.get_series("SPOT", "d", "d", "hour")
        print data

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
