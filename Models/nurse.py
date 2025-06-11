# Imports
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy


metadata = MetaData()
#db instance
db = SQLAlchemy(metadata=metadata)

class Nurse(db.model):
    __tablename__ = "nurses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.Text)



