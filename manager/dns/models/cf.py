from manager import db

class CFApiKey(db.Model):
    __tablename__ = 'cf_apikey'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    key = db.Column(db.String(64))
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
