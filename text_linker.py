#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: text_linker.py
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
from __future__ import unicode_literals
import codecs
import sys

from app.alc_etm_searcher import ALCEtmSearcher

USAGE = '''
ALC Etm Text Linker

Usage:
    $ ./text_linker.py text.txt
    Outpt: {Linked html text}

    # Save file
    $ ./text_linker.py text.txt > text.txt.html

Note: Require database
'''


def readFile(filename):
    f = codecs.open(filename, 'r', 'utf-8')
    try:
        return f.read()
    finally:
        f.close()


def main():
    if len(sys.argv) < 2:
        print('Please specify text file')
        print(USAGE)
        sys.exit()
    else:
        filename = sys.argv[1]

    text = readFile(filename)

    searcher = ALCEtmSearcher()
    linked_text = searcher.text_linker(text)
    print(linked_text)

if __name__ == '__main__':
    main()
