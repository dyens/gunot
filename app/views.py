#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-15, dyens
#
from app import app
from flask import render_template, flash, redirect, url_for
from flask import request
from forms import SheetForm, SearchSheetForm
from utils import ServiceFinder
from werkzeug import secure_filename
from models import Sheet


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

#FLASH_MESSAGES = ['message', 'info', 'warning', 'error']

@app.route('/add_sheet', methods = ['GET', 'POST'])
def add_sheet():
    form = SheetForm()
    if form.validate_on_submit():
        # TODO: upload files and create sheets from models.Sheet
        file_ = form.create_file()
        files = [file_]
        author_name = form.author.data
        arranger_name = form.arranger.data or None
        instrument_name = form.instrument.data
        name = form.name.data
        Sheet.create_sheet(
                author_name = author_name,
                arranger_name = arranger_name,
                instrument_name = instrument_name,
                name = name,
                files = files
                )
        flash(u'Файл загружен', 'message')
#        return redirect(url_for('sheets'))
    return render_template("add_sheet.html",
        title = 'List of sheets',
        form = form)

@app.route('/search_sheet', methods = ['GET', 'POST'])
def search_sheet():
    form = SearchSheetForm()
    if form.validate_on_submit():
        return redirect(url_for('sheets'))
    return render_template("search_sheet.html",
        title = 'Search sheet',
        form = form)


@app.route('/search_service', methods = ['POST'])
def search_service():
    json =  ServiceFinder().get_json(request.json)
    return json

