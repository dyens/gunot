#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-02, dyens
#

from flask import Flask
from flask.ext.testing import TestCase
from flask.ext.testing import LiveServerTestCase
from app import app, db, config

class TestApp(TestCase):

    def create_app(self):
        app.config.from_object('config')
        self.app = app.test_client()
        return app



class TestLive(LiveServerTestCase):
    u'''
    Example:

        def test_server_is_up_and_running(self):
            response = urllib2.urlopen(self.get_server_url())
            self.assertEqual(response.code, 200)
    '''

    def create_app(self):
        app.config.from_object('config')
        self.app = app.test_client()
        return app


class TestDb(TestCase):


    def create_app(self):
        app.config.from_object('config')
        self.app = app.test_client()
        return app


    def setUp(self):
        db.create_all()
        self.db = db


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestLiveWithDb(TestLive, TestDb):
    pass


class TestNotRenderTemplates(TestCase):
#    def test_assert_not_process_the_template(self):
#        response = self.client.get("/template/")
#
#        assert "" == response.data
    render_templates = False

class TestNotRenderTemplatesWithDb(TestNotRenderTemplates, TestDb):
    pass


