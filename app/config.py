#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-15, dyens
#
import os

basedir = os.path.abspath(os.path.dirname(__file__))

STATIC_FOLDER = os.path.join(basedir, 'static')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'secret_key'

UPLOAD_PATH = os.path.join(basedir, 'uploads')

TESTING = False
