#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-07-31, dyens
#
import os
from config import UPLOAD_PATH
from flask import jsonify
from models import Author, Arranger, Instrument, File, Sheet
from werkzeug import secure_filename
from app import db

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
        ret = [a.name for a in \
                Author.query.filter(Author.name.startswith(name)).limit(10)]
        return ret

    def get_sheet_arranger(self, name):
        ret = [a.name for a in \
                Arranger.query.filter(Arranger.name.startswith(name)).limit(10)]
        return ret

    def get_sheet_instrument(self, name):
        ret = [i.name for i in \
                Instrument.query.filter(Instrument.name.startswith(name)).limit(10)]
        return ret


def get_file_path(file_name, UPLOAD_PATH):
    append_version = False
    path = os.path.join(UPLOAD_PATH, file_name)
    while os.path.exists(path):
        file_name_list = file_name.split('_')
        try:
            version_str = file_name_list[0][1:]
            version = int(version_str)
        except ValueError:
            file_name_list[0] = 'v1_%s' %file_name_list[0]
            file_name = '_'.join(file_name_list)
            path = os.path.join(UPLOAD_PATH, file_name)
            continue
        version += 1
        file_name_list[0] = 'v%d' %version
        file_name = '_'.join(file_name_list)
        path = os.path.join(UPLOAD_PATH, file_name)
    return file_name, path



#def upload():
#    #TODO: write normal exception
#    form = SheetForm()
#    if form.pdf.data:
#        name = form.name.data.lower().strip()
#        if Sheet.query.filter_by(name=name).first():
#            raise Exception(u'Для данного произведения уже есть ноты')
#
#        author_name = form.author.data.lower().strip()
#        author = Author.query.filter_by(name=author_name).first()
#        if not author:
#            author = Author(name=author_name)
#            db.session.add(author)
#
#        arranger_name = form.arranger.data.lower().strip()
#        arranger = Arranger.query.filter_by(name=arranger_name).first()
#        if not arranger and arranger_name:
#            arranger = Arranger(name=arranger_name)
#            db.session.add(arranger)
#
#        instruments = []
#        instrument_names = form.instrument.data.split(',')
#        for instrument_name in instrument_names:
#            instrument_name = instrument_name.lower().strip()
#            instrument = Instrument.query.filter_by(name=instrument_name).first()
#            if not instrument:
#                instrument = Instrument(name=instrument_name)
#                db.session.add(instrument)
#            instruments.append(instrument)
#
#        #TODO: file_name
#        file_name = secure_filename(form.pdf.data.filename)
#        file_type = form.pdf.data.content_type
#        file_size = form.pdf.data.content_length
#        file_ = File(
#                file_name = file_name, file_type=file_type,
#                file_size = file_size)
#        db.session.add(file_)
#        #TODO: think about published = Bool
#        sheet = Sheet(
#                author_id=author.id,
#                arranger_id=arranger.id or None,
#                file_id=file_.id,
#                name=name,
#                published=True)
#        for insrument in instruments:
#            sheet.instruments.append(instrument)
#        db.session.add(sheet)
#        db.session.commit()
#        form.pdf.data.save(os.path.join(UPLOAD_PATH, file_name))


#        ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__iter__', '__module__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parse_content_type', 'close', 'content_length', 'content_type', 'filename', 'headers', 'mimetype', 'mimetype_params', 'name', 'save', 'stream']

