from enum import unique

from sqlalchemy.orm import backref
from voting_app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable = False)
    village = db.Column(db.String(120), nullable =False)
    date_of_birth = db.Column(db.DateTime)
    email = db.Column(db.String(120), unique=True, nullable = False)
    academic_stands = db.Column(db.String(120))
    skill_set = db.Column(db.String(60))
    is_moboho_member =db.Column(db.String(60))
    is_chief = db.Column(db.String(60))
    phone_number = db.Column(db.Integer)
    address = db.Column(db.String(120))

    
    def __repr__(self):
        return f"User('{self.name}','{self.email}','{self.is_moboho_member}')"

class Election(db.Model):
    total_aspirant = db.Column(db.Integer, primary_key =True)
    position = db.Column(db.String(60),nullable =False)
    contestant = db.Column(db.String(120), db.ForeignKey('user.name'), nullable = False)

    def __repr__(self):
        return f"Election('{self.position}','{self.contestant}')"

class Poll(db.Model):
    who_to_vote = db.Column(db.String(120), db.ForeignKey('user.name'), nullable=False)
    no_votes = db.Column(db.Integer, primary_key=True)
    check_vote = db.relationship('User', backref='votes', lazy=True)

    def __repr__(self):
        return f"Poll('{self.who_to_vote}','{self.no_votes}')"
