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

from models import Author, Arranger, MusicForm, Instrument
from models import CENTURIES

class AuthorForm(Form):
    author_name = TextField(u'Автор', validators = [Required()])


class ArrangerForm(Form):
    arranger_name = TextField(u'Аранжировщик', validators = [Required()])


class MusicFormForm(Form):
    music_form_name = TextField(u'Музыкальная форма', validators = [Required()])

class SheetForm(Form):
    name = TextField(u'Название', validators = [Required()])
    author_id = SelectField(u'Автор', [validators.required()],
            choices=[(a.id, a.name) for a in Author.query.all()], coerce=int)
    arranger_id = SelectField(u'Аранжировщик', 
            choices=[(a.id, a.name) for a in Arranger.query.all()], coerce=int)
    instruments = SelectField(u'Инструменты', [validators.required()],
            choices=[(i.id, i.name) for i in Instrument.query.all()], coerce=int)
    music_form_id = SelectField(u'Музыкальная форма', [validators.required()],
            choices=[(m.id, m.name) for m in Arranger.query.all()], coerce=int)
    century = SelectField(u'Век', choices=CENTURIES)
    pdf = FileField(u'Файл', [validators.Regexp(r'^[^/\\]\.pdf$')])


#def upload(request):
#    form = SheetForm(request.POST)
#    if form.pdf.data:
#        data = request.FILES[form.pdf.name].read()
#        open(os.path.join(UPLOAD_PATH, form.pdf.data), 'w').write(data)
