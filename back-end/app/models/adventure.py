# get it from yelp figure out what the tops ones are and then rank it


from app import db

class Adventure(db.Model): #inheriting from SQLA's model class, turning a basic python class into a SQLA model, Model syntax stays
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #model creates blueprint for table in our databse
    activity_name = db.Column(db.String) #without db.Column, we would not be able to have these columns in our task table
    likes_count = db.Column(db.Integer, default = 0)
    description = db.Column(db.String) #when we do db. init we are reading models and from there creating task table
    date = db.Column(db.TimeStamp)
    # completed_at = db.Column(db.DateTime, nullable=True) #every column in table requires data type, SQLA takes python and turns it into SQL code
    # user_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id')) #creates column in task database.,left side is name of table and right is name of column
    # user = db.relationship("Goal", back_populates="tasks")#lets flask know line 12 has special meaning to write this model
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship("Location", backref="location")
# def task_dict(self):
#     return f'{self.task_id} title:{self.title} Description: {self.description} Completed_at: {self.completed_at}'