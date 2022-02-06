from app import db

class Group(db.Model): #inheriting from SQLA's model class, turning a basic python class into a SQLA model, Model syntax stays
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #model creates blueprint for table in our databse
    group_name = db.Column(db.String) #without db.Column, we would not be able to have these columns in our task table
    user_list = db.Column(db.String)
    activity_list = db.Column(db.String)