from flask import render_template
from flask.ext.login import login_required

from .base import app
from .auth import admin_permission


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/private')
@login_required
def private():
    return render_template('private.html')


@app.route('/admin')
@login_required
@admin_permission.require()
def admin():
    return render_template('admin.html')
