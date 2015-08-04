#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-01-15, dyens
#

"""
sqlalchemy models
"""

from app import db

def get_or_create(model, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance



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
    # maybe many files for one sheet
    sheet_id = db.Column(db.Integer, db.ForeignKey('sheet.id'))

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

    def __repr__(self):
        return '<Instrument %r>' % (self.name)

class SheetName(db.Model):
    u'''
    Названия произведений
    '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True)
    sheet_id = db.Column(db.Integer, db.ForeignKey('sheet.id'))

    def __repr__(self):
        return '<SheetName %r>' % (self.name)



class Sheet(db.Model):
    u'''
    Произведения
    '''
    id = db.Column(db.Integer, primary_key = True)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    arranger_id = db.Column(db.Integer, db.ForeignKey('arranger.id'))
    files = db.relationship('File', backref='sheet',
                                lazy='dynamic')

    instruments = db.relationship('Instrument',
            secondary=instrument_sheet_association,
            backref=db.backref('sheets', lazy='dynamic'))

    names = db.relationship('SheetName', backref='sheet',
                                lazy='dynamic')

    # Sheet = Suite BWV 1, Sheet.parent = Allegro
    parent_id = db.Column(db.Integer, db.ForeignKey('sheet.id'), index=True)
    parent = db.relationship('Sheet', remote_side=id, backref='parts')

    @property
    def childrens(self):
        return Sheet.query.filter_by(parent=self)

    @staticmethod
    def create_sheet(author_name, files, instrument_names=None,
            names=None, instrument_name=None, name=None,
            parent=None, arranger_name=None):
        u'''
        author_name, arranger_name - string parameters,
        files - list of file objects,
        instrument_names - list of names of instruments,
        names - list of sheet names,
        parent - sheet object
        '''

        instruments = []
        if instrument_name:
            instrument = get_or_create(Instrument, name=instrument_name)
            instruments.append(instrument)
        elif instrument_names:
            for instrument_name in instrument_names:
                instrument = get_or_create(Instrument, name=instrument_name)
                instruments.append(instrument)
        else:
            raise TypeError(u'instrument names should be set')

        names_list = []
        if name:
            name_obj = get_or_create(SheetName, name=name)
            names_list.append(name_obj)
        elif names:
            for name in names:
                name_obj = get_or_create(SheetName, name=name)
                names_list.append(name_obj)
        else:
            raise TypeError(u'Sheet name should be set')

        author = get_or_create(Author, name=author_name)
        arranger = None
        if arranger_name:
            arranger = get_or_create(Arranger, name=arranger_name)

        sheet = Sheet(
                author=author,
                arranger=arranger,
                files=files,
                instruments=instruments,
                names=names_list,
                parent=parent
                )
        db.session.add(sheet)
        db.session.commit()
        return sheet







    def __repr__(self):
        return '<Sheet %r>' % (self.id)


