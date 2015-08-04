#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-02, dyens
#

from test import init_path
init_path()

import os
import shutil
import unittest
from utils import TestNotRenderTemplatesWithDb
from StringIO import StringIO
from app.models import Sheet, Author


#    def test_assert_not_process_the_template(self):
#        response = self.client.get("/template/")
#
#        assert "" == response.data



class TestAddSheet(TestNotRenderTemplatesWithDb):
    PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), \
            'TEST_UPLOAD')


    def setUp(self):
        os.mkdir(self.PATH)
        return super(TestAddSheet, self).setUp()

    def tearDown(self):
        super(TestAddSheet, self).tearDown()
        shutil.rmtree(self.PATH)

    def test_add(self):
        response = self.client.post('/add_sheet',
                data={
                    'name': 'name',
                    'author': 'author',
                    'arranger': 'arranger',
                    'instrument': 'instrument',
                    'pdf': (StringIO('pdfdata'), 'test.pdf')
                })
        self.assertIn('test.pdf', os.listdir(self.PATH))
        test_sheet = Sheet.query.get(1)
        self.assertEqual(test_sheet.names[0].name, 'name')
        self.assertEqual(test_sheet.author.name, 'author')
        self.assertEqual(test_sheet.arranger.name, 'arranger')
        self.assertEqual(test_sheet.instruments[0].name, 'instrument')

        response = self.client.post('/add_sheet',
                data={
                    'name': 'another_name',
                    'author': 'author',
                    'arranger': 'arranger',
                    'instrument': 'instrument',
                    'pdf': (StringIO('pdfdata'), 'test.pdf')
                })
        self.assertIn('v1_test.pdf', os.listdir(self.PATH))
        test_sheet_2 = Sheet.query.get(2)
        self.assertEqual(test_sheet_2.names[0].name, 'another_name')
        self.assertEqual(test_sheet_2.author.name, 'author')
        self.assertEqual(test_sheet_2.arranger.name, 'arranger')
        self.assertEqual(test_sheet_2.instruments[0].name, 'instrument')

        self.assertEqual(test_sheet_2.author, test_sheet.author)
        self.assertEqual(test_sheet_2.arranger, test_sheet.arranger)
        self.assertEqual(test_sheet_2.instruments[0], test_sheet.instruments[0])

        self.assertEqual(len(Author.query.all()), 1)







if __name__ == '__main__':
    unittest.main()
