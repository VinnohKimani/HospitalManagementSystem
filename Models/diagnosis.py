from sqlalchemy import MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from patient import Patients

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Diagnosis(db.Model):
    __talename__ = "diagnoses"

    id = db.Column(db.Integer, primary_key=True)
    diagnosis_note = db.Column(db.Text)
    patient_id = db.Column(db.Integer, ForeignKey(Patients.id))
