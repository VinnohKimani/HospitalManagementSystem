from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)


class Prescriptions(db.model):
    __tablename__ = "prescriptions"

    id = db.Column(db.Integer, Primary_Key=True)
    name = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
