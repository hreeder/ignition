from manager import db

class CFDomain(db.Model):
    __tablename__ = 'cf_domain'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    key = db.Column(db.Integer, db.ForeignKey('cf_apikey.id'))

class CFDomainAccess(db.Model):
    __tablename__ = 'cf_domain_access'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    domain_id = db.Column(db.Integer, db.ForeignKey('cf_domain.id'))
