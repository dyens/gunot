#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-04, dyens
#
from test import init_path
init_path()
import unittest
from app.forms import SheetForm
import os
import shutil
from utils import TestDb


class FILE_(object):
    FILE_NAME = None
    CONTENT_TYPE = None
    CONTENT_LENGTH = None

    def __init__(self, file_name, content_type='pdf', content_length=12):
        self.FILE_NAME = file_name
        self.CONTENT_TYPE = content_type
        self.CONTENT_LENGTH = content_length

    @property
    def filename(self):
        return self.FILE_NAME

    @property
    def content_type(self):
        return self.CONTENT_TYPE

    @property
    def content_length(self):
        return self.CONTENT_LENGTH

    def save(self, path):
        with open(path, 'w') as f:
            pass




class TestSheetFormUpload(TestDb):
    PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), \
            'TEST_UPLOAD')


    def setUp(self):
        os.mkdir(self.PATH)
        return super(TestSheetFormUpload, self).setUp()

    def tearDown(self):
        super(TestSheetFormUpload, self).tearDown()
        shutil.rmtree(self.PATH)


    def test_upload(self):
        form = SheetForm(
                name=u'BWV1001',
                autor=u'Bach',
                pdf=FILE_(file_name=u'test.pdf'))
        form.create_file()
        self.assertTrue(os.path.exists(os.path.join(self.PATH, 'test.pdf')))
        form = SheetForm(
                name=u'BWV1001',
                autor=u'Bach',
                pdf=FILE_(file_name=u'test.pdf'))
        form.create_file()
        self.assertTrue(os.path.exists(os.path.join(self.PATH, 'v1_test.pdf')))
        form = SheetForm(
                name=u'BWV1001',
                autor=u'Bach',
                pdf=FILE_(file_name=u'v1_test.pdf'))
        form.create_file()
        self.assertTrue(os.path.exists(os.path.join(self.PATH, 'v2_test.pdf')))
        


if __name__ == '__main__':
    unittest.main()
