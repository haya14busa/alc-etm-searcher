#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: app/views.py
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

from app import app
from flask import render_template, request, redirect, url_for
from flask import Markup

from app.alc_etm_searcher import ALCEtmSearcher


@app.route('/')
def index():
    search_word = request.args.get('search_word', '')
    is_found = request.args.get('is_found', True)
    return render_template('index.html',
                           search_word=search_word,
                           is_found=is_found)


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Create an instance of ALCEtmSearcher
# FIXME: maybe there are more clever ways
try:
    searcher = ALCEtmSearcher()
except Exception as e:
    # To show index page even if searcher does not work
    # FIXME: does it really work?
    app.logger.error(e)


@app.route('/send_word', methods=['GET', 'POST'])
def send_word():
    # Get word: Support both GET and POST methods
    search_word = request.values.get('search_word', '')
    # Early Return if search_word is empty
    if search_word == '':
        return redirect(url_for('index'))
    # Get word data from database
    word_data = searcher.find_word_with_unum(search_word)
    if word_data:
        # Redirect to ALC page if word data is found
        return redirect(searcher.url_unum.format(
            unum=word_data['alc_etm']['unum']))
    else:
        # Redirect to index if word data is not found
        return redirect(url_for('index',
                                is_found=False,
                                search_word=search_word))


@app.route('/text_linker', methods=['GET', 'POST'])
def text_linker():
    if request.method == 'GET':
        return render_template('text_linker.html', link_text=None)

    if request.method == 'POST':
        text = request.form['search_text']
        link_text = searcher.text_linker(text, is_newtab=False)
        return render_template('text_linker.html', link_text=Markup(link_text))
