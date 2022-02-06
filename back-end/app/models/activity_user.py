from app import db

class ActivityUser(db.Model):
    __tablename__ = "activity_user"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True,nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), primary_key=True,nullable=False)
