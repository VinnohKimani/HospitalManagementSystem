from sqlalchemy import MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from doctors import Doctor

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Patients(db.model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, Primary_Key=True)
    name = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Integer)
    history = db.Column(db.String)
    doctor_id = db.Column(db.integer, ForeignKey(Doctor.id))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Patient {self.name} {self.history}>"
