from db import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    age = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    height = db.Column(db.String(80), nullable=False)
    foot = db.Column(db.String(10), nullable=False)
    club = db.Column(db.String(80), nullable=False)
    market_value = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Player %r>' % self.name
