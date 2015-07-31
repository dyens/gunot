#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-15, dyens
#

"""
sqlalchemy models
"""

from app import db


class Author(db.Model):
    u'''
    Авторы
    '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True)
    sheets = db.relationship('Sheet', backref=u'author', lazy='dynamic')

    def __repr__(self):
        return '<Author %r>' % (self.name)

class Arranger(db.Model):
    u'''
    Аранжировщики
    '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True)
    sheets = db.relationship('Sheet', backref=u'arranger', lazy='dynamic')

    def __repr__(self):
        return '<Arranger %r>' % (self.name)

class File(db.Model):
    u'''
    Файлы
    '''
    id = db.Column(db.Integer, primary_key = True)
    # name будет равно id
    file_name = db.Column(db.String(120))
    # content-type
    # https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_MIME-%D1%82%D0%B8%D0%BF%D0%BE%D0%B2#application
    file_type = db.Column(db.String(120))
    file_size = db.Column(db.Integer)
    # one to one relationship (uselist = False)
    sheet = db.relationship('Sheet', backref=u'file', uselist=False)

    def __repr__(self):
        return '<File %r>' % (self.file_name)


instrument_sheet_association = db.Table('instrument_sheet',
    db.Column('instrument_id', db.Integer, db.ForeignKey('instrument.id')),
    db.Column('sheet_id', db.Integer, db.ForeignKey('sheet.id'))
)


class Instrument(db.Model):
    u'''
    Инструменты
    '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True)

class Sheet(db.Model):
    u'''
    Произведения
    '''
    id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    arranger_id = db.Column(db.Integer, db.ForeignKey('arranger.id'))
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    instruments = db.relationship("Instrument", 
            secondary=instrument_sheet_association,
            backref=db.backref('sheets', lazy='dynamic'))
    name = db.Column(db.String(120), index = True)
    published = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Sheet %r - %r>' % (self.author, self.name)


