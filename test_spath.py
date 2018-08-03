#!/usr/bin/env python

import unittest
import spath


class TestSPath(unittest.TestCase):
    def test_moves(self):
        for m in spath.next_moves((0, 0)):
            print m

        for m in spath.next_moves((3, 3)):
            print m

    def test_shortest_path(self):
        spath.shortest_path((0, 0), (7, 0))
