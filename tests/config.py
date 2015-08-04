#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-15, dyens
#
import os

basedir = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(basedir, 'static')
LIVESERVER_PORT = 8943
SQLALCHEMY_DATABASE_URI = "sqlite://"
CSRF_ENABLED = False
UPLOAD_PATH = os.path.join(basedir, 'TEST_UPLOAD')
TESTING = True

WTF_CSRF_ENABLED = False
