#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: app/database.py
# AUTHOR: haya14busa
# License: MIT license
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#=============================================================================

from pymongo import Connection
import os
from urllib.parse import urlsplit


class WordDB(object):
    ''' Etymology Word DataBase '''
    def __init__(self, db_name):
        self.db = self.connect2mongodb(db_name)

    def connect2mongodb(self, db_name=None):
        MONGO_URL = os.environ.get('MONGOHQ_URL', None)
        if MONGO_URL:  # For heroku
            c = Connection(host=MONGO_URL, port=27017)
            parsed = urlsplit(MONGO_URL)
            db_name = parsed.path[1:]
            return c[db_name]
        else:
            c = Connection(host='localhost', port=27017)
            return c[db_name]

    def find_in_alc_etm(self, word, field):
        # db = connect2mongodb('mydict')
        return self.db.words.find_one({field: word}, {'alc_etm.unum': 1})


def main():
    db = WordDB('mydict')
    print(db.find_in_alc_etm('polish', 'lemma'))
    print(db.find_in_alc_etm('polishing', 'lemma'))

if __name__ == '__main__':
    main()
