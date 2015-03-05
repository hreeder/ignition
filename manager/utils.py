import requests

from functools import wraps
from flask import current_app, flash, request, abort
from flask.ext.login import current_user

def send_email(to, subject, text_body, html_body):
    data = {
        "from": current_app.config['MG_FROM'],
        "to": to,
        "subject": subject,
        "text": text_body,
        "html": html_body
    }

    requests.post(
        current_app.config['MG_ENDPOINT'],
        auth=("api", current_app.config['MG_API']),
        data=data
    )

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

def superuser_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user is None:
            return redirect(url_for('login', next=request.url))
        elif not current_user.superuser:
            abort(403)
        else:
            return f(*args, **kwargs)
    return decorated_function
