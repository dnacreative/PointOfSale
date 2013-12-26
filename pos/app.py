from __future__ import absolute_import

from flask import Flask, render_template

import pos.app_settings

app = Flask('pos')

@app.route('/')
def root():
    return render_template('index.html')
    
@app.route('/inventory/')
def inventory():
    # TODO: build list of items to display
    items = [{'id': 1, 'name': 'magnetic bookmark', 'description': 'watercolor bookmark', 'vendor_code': 'N/A', 'dept_code': 'N/A', 'quantity': 12, 'tax': True, 'cost': 1.00, 'price': 1.99}]
    return render_template('invn.html', items=items)
    
@app.route('/inventory/<int:id>')
def show_item(id):
    # detail page for item
    return render_template('invn.html')