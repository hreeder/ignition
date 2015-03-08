from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_required, current_user

from manager.dns import dns
from manager.dns.models import CFApiKey, CFDomain, CFDomainAccess

@dns.route("/")
@login_required
def home():
    keys = CFApiKey.query.filter_by(owner=current_user.id).all()
    domains = []

    for key in keys:
        domains.extend(CFDomain.query.filter_by(key=key).all())
    return render_template("dns/home.html",domains=domains)

@dns.route("/add")
@login_required
def add_domain():
    return render_template("dns/add.html")

@dns.route("/keys")
@login_required
def view_keys():
    return render_template("dns/view_keys.html")