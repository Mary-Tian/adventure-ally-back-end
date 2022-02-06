from app import db

class GroupActivity(db.Model):
    __tablename__ = "group_activity"
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True,nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), primary_key=True,nullable=False)