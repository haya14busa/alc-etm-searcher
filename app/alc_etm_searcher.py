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
        self.url_unum = \
            'http://home.alc.co.jp/db/owa/etm_sch?unum={unum}&stg=2'

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

    def text_linker(self, text, is_newtab=None):
        # link_format = '<a href="{url}" target="_blank">{w}</a>'.format(
        target = 'target="_blank"' if is_newtab else ''
        link_format = '<a href="{url}" {target}>{w}</a>'.format(
            url=self.url_unum, w='{w}', target=target)

        # Cache linked word not to look into database more hantwice
        # {word: unum}
        # NOTE: Should it be with MongoDB or something?
        linked_word = {}

        sentences = text.splitlines()
        sentence_list = []
        for sentence in sentences:
            word_list = []
            for word in self.n.tokenize(sentence):
                # Filter stopwords
                if len(word) < 3 or word.lower() in self.n.stopwords:
                    word_list.append(word)
                    continue
                # Not to look into database twice with the same word
                if word in linked_word:
                    word_list.append(
                        link_format.format(
                            unum=linked_word[word],
                            w=word
                        ))
                    continue
                # Try to find word in DataBase
                word_data = self.find_word_with_unum(word.lower())
                if word_data:
                    linked_word[word] = word_data['alc_etm']['unum']
                    word_list.append(
                        link_format.format(
                            unum=word_data['alc_etm']['unum'],
                            w=word
                        ))
                else:
                    word_list.append(word)
            sentence_list.append(' '.join(word_list))
        return '<br>'.join(sentence_list)
