#!/usr/bin/env python

# Flask-Assets is causing issues here right now
# I've commented out the offending lines, until
# it can be fixed.

#from flask.ext.assets import ManageAssets
from flask.ext.migrate import MigrateCommand
from flask.ext.script import Manager
from manager import app

manage = Manager(app)

#manage.add_command("assets", ManageAssets(assets))
manage.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manage.run()
