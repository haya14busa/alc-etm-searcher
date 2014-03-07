#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: app/nlp.py
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
''' Natural Language Processing '''


from nltk.corpus import stopwords
from nltk import stem
from nltk import tokenize


class NLTK(object):
    def __init__(self):
        self.stopwords = stopwords.words('english')
        self._lancaster = stem.LancasterStemmer()
        self._porter = stem.PorterStemmer()
        self._lemmatizer = stem.WordNetLemmatizer()

    def lancaster_stemmer(self, word):
        return self._lancaster.stem(word)

    def porter_stemmer(self, word):
        return self._porter.stem(word)

    def lemmatizer(self, word):
        return self._lemmatizer.lemmatize(word)

    def tokenize(self, sentence):
        return tokenize.wordpunct_tokenize(sentence)


def main():
    n = NLTK()
    print(n.lancaster_stemmer('polished'))
    print(n.porter_stemmer('polished'))
    print(n.lemmatizer('polished'))

if __name__ == '__main__':
    main()
