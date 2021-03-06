#!/usr/bin/env python
# encoding: utf-8
"""
Base modules used by test cases.
 
=======================================================================
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
=======================================================================
"""


import unittest
from datetime import datetime


class TestCaseBase(unittest.TestCase):
    """Base from which all test cases should inherit."""
    
    def setUp(self):
        """Setup for all test cases."""
        self.startts = datetime.now()
        print("[{}] Running {} ...".format(str(self.startts)[:-7], self.id()))
    
    def tearDown(self):
        """Cleanup for all test cases."""
        self.endts = datetime.now()
