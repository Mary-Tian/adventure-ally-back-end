from app import db

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    likes_count = db.Column(db.Integer, default = 0)
    title = db.Column(db.String)
    user = db.relationship("Favorite", backref="user")
    def favorite_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "user": self.user,
            "likes_count": self.likes_count
        }