from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Text)
    
    # title = db.Column(db.String)
    adventure = db.relationship("Adventure", backref="user", lazy = True, )