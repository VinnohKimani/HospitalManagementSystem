from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

metadata = MetaData()

db  = SQLAlchemy(metadata= metadata)

class Daignosis(db.Model):
    __talename__ = "diagnoses"

    id = db.Column(db.Integer, primary_key= True)
    diagnosis_note = db.Column(db.Text)

