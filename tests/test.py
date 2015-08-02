#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-02, dyens
#

import unittest
from utils import TestApp, TestDb
from app.models import Author
from app import db


class TestExample(TestApp):

    def test_example(self):
        pass

class TestDbExample(TestDb):

    def test_example(self):
        a = Author(name=u'Вася')
        db.session.add(a)
        db.session.commit()
        vasya = a.query.filter_by(name=u'Вася').first()
        self.assertEqual(u'Вася', vasya.name)
        vasya = a.query.get(1)
        self.assertEqual(u'Вася', vasya.name)



if __name__ == '__main__':
    unittest.main()
