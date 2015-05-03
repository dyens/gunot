#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-15, dyens
#

"""
init application
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')
db = SQLAlchemy(app)
from app import views, models
