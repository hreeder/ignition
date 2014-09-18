from manager import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(256))
    enabled = db.Column(db.Boolean)
    superuser = db.Column(db.Boolean)
    openid_enabled = db.Column(db.Boolean)

    def is_authenticated():
        return True

    def is_active():
        return self.enabled

    def is_anonymous():
        return False

    def get_id():
        return self.id
