from app import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_name = db.Column(db.String)
    # each location can have many activities, but each adventure has one location
    # books = db.relationship("Book", back_populates="author")
    adventure = db.relationship("Adventure", backref="location")
    