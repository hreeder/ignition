from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_required

from manager.dns import dns
from manager.dns.models import CFApiKey, CFDomain, CFDomainAccess

@dns.route("/")
@login_required
def home():
    domains = [
        {
            'name': 'f-t.so',
            'id': 1
        },
        {
            'name': 'butts.so',
            'id': 2
        },
        {
            'name': 'f-t.so',
            'id': 3
        },
        {
            'name': 'f-t.so',
            'id': 4
        },
        {
            'name': 'f-t.so',
            'id': 5
        },
    ]
    return render_template("dns/home.html",domains=domains)

@dns.route("/add")
@login_required
def add_domain():
    return render_template("dns/add.html")

@dns.route("/keys")
@login_required
def view_keys():
    return render_template("dns/view_keys.html")