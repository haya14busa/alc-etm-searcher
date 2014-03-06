#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: app/alc_etm_searcher.py
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

from app.database import WordDB
from app.nlp import NLTK


class ALCEtmSearcher(object):
    def __init__(self):
        self.db = WordDB('mydict')
        self.n = NLTK()

    def find_word_with_unum(self, word):
        ''' Aggressively find word data of ALC etmology dictionary with NLP
        1. word itself
        2. lemmatize
        3. Porter stemmer with lemma
        4. Porter stemmer with stem
        5. Lancaster stemmer with stem
        '''
        lemma = self.n.lemmatizer(word)
        p_stem = self.n.porter_stemmer(word)
        l_stem = self.n.lancaster_stemmer(word)
        word_data = self.db.find_with_unum(word, 'lemma') \
            or self.db.find_with_unum(lemma, 'lemma') \
            or self.db.find_with_unum(p_stem, 'lemma') \
            or self.db.find_with_unum(p_stem, 'stem') \
            or self.db.find_with_unum(l_stem, 'stem')
        return word_data


def main():
    alc_etm_searcher = ALCEtmSearcher()
    print(alc_etm_searcher.find_word_with_unum('polished'))

if __name__ == '__main__':
    main()
