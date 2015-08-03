#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-08-02, dyens
#

from test import init_path
init_path()

import unittest
from utils import TestApp, TestDb
from app.models import Author, Arranger, File
from app.models import Instrument, SheetName, Sheet
from app import db


class TestAuthor(TestDb):

    def test_add(self):
        author = Author(name=u'Вася')
        db.session.add(author)
        db.session.commit()
        vasya = Author.query.get(1)
        self.assertEqual(u'Вася', vasya.name)

class TestArranger(TestDb):

    def test_add(self):
        arranger = Arranger(name=u'Вася')
        db.session.add(arranger)
        db.session.commit()
        vasya = Arranger.query.get(1)
        self.assertEqual(u'Вася', vasya.name)

class TestFile(TestDb):

    def test_add(self):
        file_ = File(file_name=u'test.pdf',
                file_type=u'pdf',
                file_size=12)
        db.session.add(file_)
        db.session.commit()
        f = File.query.get(1)
        self.assertEqual(u'test.pdf', f.file_name)
        self.assertEqual(u'pdf', f.file_type)
        self.assertEqual(12, f.file_size)

class TestInstrument(TestDb):

    def test_add(self):
        instrument = Instrument(name=u'guitar')
        db.session.add(instrument)
        db.session.commit()
        guitar = Instrument.query.get(1)
        self.assertEqual(u'guitar', guitar.name)

class TestSheetName(TestDb):

    def test_add(self):
        sheet_name = SheetName(name=u'BWV 1001')
        db.session.add(sheet_name)
        db.session.commit()
        bwv_1001 = SheetName.query.get(1)
        self.assertEqual(u'BWV 1001', bwv_1001.name)

class TestSheet(TestDb):

    def add_author(self, author_name):
        author = Author(name=author_name)
        db.session.add(author)
        # TODO: Need this??
        #db.session.commit()
        return author

    def add_arranger(self, arranger_name):
        arranger = Arranger(name=arranger_name)
        db.session.add(arranger)
        #db.session.commit()
        return arranger

    def add_file(self, file_name, file_type='pdf', file_size=10):
        file_ = File(
                file_name=file_name,
                file_type=file_type,
                file_size=file_size
                )
        db.session.add(file_)
        #db.session.commit()
        return file_
    
    def add_instrument(self, instrument_name):
        instrument = Instrument(name=instrument_name)
        db.session.add(instrument)
        #db.session.commit()
        return instrument

    def add_sheet_name(self, sheet_name):
        sheet_name = SheetName(name=sheet_name)
        db.session.add(sheet_name)
        #db.session.commit()
        return sheet_name

    def add_sheet(self):
        sheet = Sheet()
        db.session.add(sheet)
        return sheet

    def test_add(self):
        sheet = self.add_sheet()
        test_sheet = Sheet.query.get(1)
        self.assertIsInstance(test_sheet, Sheet)
        test_sheet = Sheet.query.get(2)
        self.assertIsNone(test_sheet)
    
    def test_add_with_author(self):
        author = self.add_author(u'Bach')
        sheet = Sheet(author=author)
        self.assertEqual(u'Bach', sheet.author.name)
        db.session.add(sheet)
        test_sheet = Sheet.query.get(1)
        self.assertEqual(u'Bach', test_sheet.author.name)

    def test_add_with_arranger(self):
        arranger = self.add_arranger(u'Bream')
        sheet = Sheet(arranger=arranger)
        self.assertEqual(u'Bream', sheet.arranger.name)
        db.session.add(sheet)
        test_sheet = Sheet.query.get(1)
        self.assertEqual(u'Bream', test_sheet.arranger.name)

    def test_add_with_files(self):
        file_1 = self.add_file(u'file1')
        file_2 = self.add_file(u'file2')
        sheet = Sheet()
        sheet.files.append(file_1)
        sheet.files.append(file_2)
        self.assertEqual(sheet.files.count(), 2)

    def test_add_with_names(self):
        name1 = self.add_sheet_name(u'BWV 1001')
        name2 = self.add_sheet_name(u'Suite 1001')
        sheet = Sheet()
        sheet.names.append(name1)
        sheet.names.append(name2)
        self.assertEqual(2, sheet.names.count(), 2)

    def test_add_with_names_2(self):
        name1 = self.add_sheet_name(u'BWV 1001')
        name2 = self.add_sheet_name(u'Suite 1001')
        sheet = Sheet(names = [name1, name2])
        self.assertEqual(2, sheet.names.count(), 2)

    def test_add_with_instruments(self):
        sheet1 = Sheet()
        sheet2 = Sheet()
        guitar = self.add_instrument('guitar')
        piano = self.add_instrument('piano')
        voice = self.add_instrument('voice')
        sheet1.instruments.append(guitar)
        sheet1.instruments.append(piano)
        sheet2.instruments.append(guitar)
        sheet2.instruments.append(piano)
        sheet2.instruments.append(voice)
        self.assertEqual(len(sheet1.instruments), 2)
        self.assertEqual(len(sheet2.instruments), 3)

    def test_add_with_parrent(self):
        sheet1 = Sheet()
        db.session.add(sheet1)
        sheet2 = Sheet(parent=sheet1)
        self.assertEqual(sheet1.childrens.first(), sheet2)

    def test_create_sheet(self):
#        author_name, arranger_name - string parameters,
#        files - list of file objects,
#        instrument_names - list of names of instruments,
#        names - list of sheet names,
#        parent - sheet object
        test_file = self.add_file('file.pdf')
        db.session.commit()
        data = {
                'author_name': u'Bach',
                'arranger_name': u'Bream',
                'files': [test_file],
                'instrument_names': [u'guitar'],
                'names': ['BWV 1001']
                }
        Sheet.create_sheet(**data)
        self.assertEqual(len(Sheet.query.all()), 1) 
        test_sheet = Sheet.query.get(1)
        self.assertEqual(test_sheet.author.name, 'Bach') 
        self.assertEqual(test_sheet.arranger.name, 'Bream') 
        self.assertIn(test_file, test_sheet.files) 
        guitar = Instrument.query.filter_by(name='guitar').first()
        self.assertIn(guitar, test_sheet.instruments) 
        names = [i.name for i in test_sheet.names]
        self.assertIn('BWV 1001', names) 

        test_file2 = self.add_file('file.pdf')
        db.session.commit()
        data2 = {
                'author_name': u'Bach',
                'arranger_name': u'Bream',
                'files': [test_file2],
                'instrument_names': [u'guitar'],
                'names': ['Allegro'],
                'parent': test_sheet
                }
        test_sheet2 = Sheet.create_sheet(**data2)
        self.assertEqual(test_sheet2.parent, test_sheet)
        self.assertIn(test_sheet2, test_sheet.childrens)

    def test_create_simple_sheet(self):
        test_file = self.add_file('file.pdf')
        db.session.commit()
        data = {
                'author_name': u'Bach',
                'arranger_name': u'Bream',
                'files': [test_file],
                'instrument_name': u'guitar',
                }
        with self.assertRaises(TypeError):
            Sheet.create_sheet(**data)

        data = {
                'author_name': u'Bach',
                'arranger_name': u'Bream',
                'files': [test_file],
                'name': 'BWV 1001'
                }
        with self.assertRaises(TypeError):
            Sheet.create_sheet(**data)

        data = {
                'author_name': u'Bach',
                'arranger_name': u'Bream',
                'files': [test_file],
                'instrument_name': u'guitar',
                'name': 'BWV 1001'
                }
        Sheet.create_sheet(**data)
        self.assertEqual(len(Sheet.query.all()), 1) 
        test_sheet = Sheet.query.get(1)
        self.assertEqual(test_sheet.author.name, 'Bach') 
        self.assertEqual(test_sheet.arranger.name, 'Bream') 
        self.assertIn(test_file, test_sheet.files) 
        guitar = Instrument.query.filter_by(name='guitar').first()
        self.assertIn(guitar, test_sheet.instruments) 
        names = [i.name for i in test_sheet.names]
        self.assertIn('BWV 1001', names) 

    def test_create_without_arranger(self):
        test_file = self.add_file('file.pdf')
        db.session.commit()
        data = {
                'author_name': u'Bach',
                'files': [test_file],
                'instrument_name': u'guitar',
                'name': 'BWV 1001'
                }
        Sheet.create_sheet(**data)
        self.assertEqual(len(Sheet.query.all()), 1) 






if __name__ == '__main__':
    unittest.main()
