# Imports
from Models.db import db
# This allows us to define tables and their columns
# Doing this for Readability

# metadata = MetaData()

# # db instance
# db = SQLAlchemy(metadata=metadata)


class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    specialization = db.Column(db.Text)
