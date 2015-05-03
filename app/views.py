#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-15, dyens
#
from flask import render_template, flash, redirect, url_for
from flask import request
from flask import jsonify

from app import app



from forms import SheetForm
from models import Author


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    posts = [ # список выдуманных постов
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/sheets')
def sheets():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    data = [ # список выдуманных постов
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("sheets.html",
        title = 'list of sheets',
        user = user,
        data = data)

@app.route('/add_sheet', methods = ['GET', 'POST'])
def add_sheets():
    form = SheetForm()
    if form.validate_on_submit():
        flash(u'Файл загружен')
        return redirect(url_for('sheets'))
    return render_template("add_sheet.html",
        title = 'List of sheets',
        form = form)


class ServiceFinder(object):
    def get(self, json):
        error = None
        response = []
        get = json.get('get', None)
        if get is not None and get.startswith('get_sheet_'):
            request = json.get('request', None)
            if request is not None:
                func = getattr(self, get, None)
                if func is not None:
                    try:
                        response = func(request)
                    except Exception as e:
                        error = e.message
                    answer = {'response': response,
                              'error': error}
                    return answer
        error = 'wrong service request'
        answer = {'error': error}
        return answer

    def get_json(self, json):
        return jsonify(self.get(json))

    def get_sheet_name(self, name):
        return ['a', 'b', 'c']
    def get_sheet_author(self, name):
        pass
    def get_sheet_arranger(self, name):
        pass
    def get_sheet_music_form(self, name):
        pass
    def get_sheet_instrument(self, name):
        pass

@app.route('/search_service', methods = ['POST'])
def search_service():
    a =  ServiceFinder().get_json(request.json)
    print a
    return a

