#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-04, dyens
#
from test import init_path
init_path()
import unittest
from app.utils import get_file_path
import os
import shutil

class TestGetFilePath(unittest.TestCase):
    PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), \
            'TEST_UPLOAD')


    def setUp(self):
        os.mkdir(self.PATH)

    def tearDown(self):
        shutil.rmtree(self.PATH)


    def test(self):
        file_name, path = get_file_path('test.pdf', self.PATH)
        with open(path, 'w') as f:
            pass
        file_name, path = get_file_path('test.pdf', self.PATH)
        self.assertEqual(file_name, 'v1_test.pdf')
        with open(path, 'w') as f:
            pass
        file_name, path = get_file_path('v1_test.pdf', self.PATH)
        self.assertEqual(file_name, 'v2_test.pdf')
        with open(path, 'w') as f:
            pass
        file_name, path = get_file_path('test.pdf', self.PATH)
        self.assertEqual(file_name, 'v3_test.pdf')



if __name__ == '__main__':
    unittest.main()
