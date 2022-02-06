from app import db

class UserGroup(db.Model):
    __tablename__ = "user_group"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True,nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True,nullable=False)
