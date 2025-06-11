from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

class Prescriptions(db.model):
    __tablename__ ="prescriptions"
    id = db.Column(db.Integer, Primary_Key =True)
    name = db.Column(db.Text, nullable = False)
    created_at =db.Column(db.TimeStamp, default =)