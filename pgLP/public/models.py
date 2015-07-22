from pgLP.extensions import db


class EmailLead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    contactFurther = db.Column(db.Boolean)

    def __init__(self, username, email, contactFurther):
        self.username = username
        self.email = email
        self.contactFurther = contactFurther

    def __repr__(self):
        return '<User %r>' % self.email
