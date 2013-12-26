from __future__ import absolute_import

from flask import Flask, render_template

import pos.app_settings

app = Flask('pos')

@app.route('/')
def root():
    return render_template('index.html')
    
@app.route('/inventory/')
def inventory():
    return render_template('invn.html')
    
@app.route('/inventory/<int:id>')
def show_item(id):
    # detail page for item
    return render_template('invn.html')