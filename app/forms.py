#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-16, dyens
#
import re
import os
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField, FileField
from wtforms.validators import Required
from wtforms import validators
from models import Author, Arranger, Instrument, File
from utils import get_file_path
from werkzeug import secure_filename
from app import db
from app import app


class AuthorForm(Form):
    author_name = TextField(u'Автор', validators = [Required()])


class ArrangerForm(Form):
    arranger_name = TextField(u'Аранжировщик', validators = [Required()])




class SheetForm(Form):
    name = TextField(u'Название', validators = [Required()])
    author = TextField(u'Автор', validators = [Required()])
    arranger = TextField(u'Аранжировщик')
    instrument = TextField(u'Инструменты', validators = [Required()])
    pdf = FileField(u'Файл')
    
    def create_file(self):
        # TODO: think about saved file names!!
        # mb md5 ??
        file_name = secure_filename(self.pdf.data.filename)
        file_name, path = get_file_path(file_name, app.config['UPLOAD_PATH'])
        file_type = self.pdf.data.content_type
        file_size = self.pdf.data.content_length
        file_ = File(
                file_name = file_name, file_type=file_type,
                file_size = file_size)
        db.session.add(file_)
        db.session.commit()
        self.pdf.data.save(path)
        return file_




class SearchSheetForm(Form):
    name = TextField(u'Название', validators = [Required()])
    author = TextField(u'Автор', validators = [Required()])
    arranger = TextField(u'Аранжировщик')
    instrument = TextField(u'Инструменты', validators = [Required()])


