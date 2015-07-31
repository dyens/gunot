#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-16, dyens
#
import re
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField, FileField
from wtforms.validators import Required
from wtforms import validators
from models import Author, Arranger, Instrument

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

class SearchSheetForm(Form):
    name = TextField(u'Название', validators = [Required()])
    author = TextField(u'Автор', validators = [Required()])
    arranger = TextField(u'Аранжировщик')
    instrument = TextField(u'Инструменты', validators = [Required()])


