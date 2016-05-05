import os

from flask import Flask, redirect, request, url_for
from flask.ext.babel import Babel
from flask.ext.login import LoginManager, current_user
from flask.ext.principal import Identity, Permission, PermissionDenied, Principal
from ..model import Account, db


app = Flask('skeleton')  # __NAME__
app.config.from_object('{}.settings'.format(app.import_name))

babel = Babel(app)
login_manager = LoginManager(app)
principal = Principal(app, use_sessions=False, skip_static=True)

admin_role = Permission('admin')


@app.template_global()
def sign_in_url():
    if app.config['DEVELOPMENT']:
        return url_for('auth.sign_in', next=request.url)
    return url_for(
        'auth.sign_in',
        mode='select',
        next=url_for('auth.signed_in', next=request.url))


@login_manager.user_loader
def load_user(id):
    return Account.query.get(id)


@login_manager.unauthorized_handler
def authentication_required():
    return redirect(sign_in_url())


@principal.identity_loader
def load_identity():
    user = current_user._get_current_object()
    identity = Identity(user.get_id())
    if user.is_authenticated and user.is_admin:
        identity.provides.add('admin')
    return identity


@app.errorhandler(PermissionDenied)
def permission_denied(exc):
    return 'Forbidden', 403
