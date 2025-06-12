# Imports
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

# This allows us to define tables and their columns
metadata = MetaData()

# db instance
db = SQLAlchemy(metadata=metadata)


class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    specialization = db.Column(db.Text)
