from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_required

from manager.dns import dns
from manager.dns.models import CFApiKey, CFDomain, CFDomainAccess

@dns.route("/")
@login_required
def home():
    return render_template("dns/home.html")
