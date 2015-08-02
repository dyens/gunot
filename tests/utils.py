#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-02, dyens
#

from flask import Flask
from flask.ext.testing import TestCase
from flask.ext.testing import LiveServerTestCase
from app import db

class TestApp(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app



class TestLive(LiveServerTestCase):
    u'''
    Example:

        def test_server_is_up_and_running(self):
            response = urllib2.urlopen(self.get_server_url())
            self.assertEqual(response.code, 200)
    '''

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        return app


class TestDb(TestApp):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        return super(TestDb, self).create_app()

    def setUp(self):
        db.create_all()
        self.db = db


    def tearDown(self):
        db.session.remove()
        db.drop_all()


