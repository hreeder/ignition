#!/usr/bin/env python
from flask.ext.assets import ManageAssets
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from manager import app, assets, db

manage = Manager(app)
migrate = Migrate(app, db)

manage.add_command("assets", ManageAssets(assets))
manage.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manage.run()
