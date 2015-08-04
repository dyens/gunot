#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-02, dyens
#
import os, sys
import unittest
import testoob


def init_path():
    TEST_DIR = os.path.abspath(os.path.dirname(__file__))
    APP_DIR = os.path.split(TEST_DIR)[0]
    PYTHON_PATH = sys.path
    if APP_DIR not in PYTHON_PATH:
        PYTHON_PATH.append(APP_DIR)
    if TEST_DIR not in PYTHON_PATH:
        PYTHON_PATH.append(TEST_DIR)


if __name__ == "__main__":
    init_path()
    testdir = os.path.split(__file__)[0]
    testfiles = \
        [f[:-3] for f in os.listdir(testdir or ".") \
         if f.startswith('test_') and f.endswith('.py')]
    modules = [__import__(file_) for file_ in testfiles]
    test_loader = unittest.TestLoader()
    tests = [test_loader.loadTestsFromModule(module) for module in modules]
    suite = unittest.TestSuite(tests)
    testoob.main(suite)
