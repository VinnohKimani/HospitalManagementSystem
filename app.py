from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from models import db


app = Flask(__name__)
# Cofiguring flask app using config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospitalManagementSystem.db"
app.config["SQLALCHEMY_ECHO"] = True

# Links db to flask app
db.init_app(app)

# import models
from models.doctors import Doctor
from models.patient import Patients
from models.nurse import Nurse
from models.prescription import Prescriptions
from models.diagnosis import Diagnosis
# from Models.appointment import *
# from Models.billing import *

# import resources
from resources.doctors import DoctorResource
from resources.patient import PatientResource
from resources.nurse import NurseResource
from resources.appointment import AppointmentResource
from resources.billing import BillResource
# from resources.diagnosis import DiagnosisResource
# from resources.prescriptions import PrescriptionsResource


# Linking flask resfull with app
api = Api(app)

# create migrations
migrate = Migrate(app, db)


# Routes
@app.route("/")
def index():
    return {"message": "Welcome to our hospital API"}


api.add_resource(DoctorResource, "/doctors", "/doctors/<int:id>")
api.add_resource(PatientResource, "/patients", "/patients/<int:id>")
api.add_resource(NurseResource, "/nurses", "/nurses/<int:id>")
api.add_resource(AppointmentResource, "/appointments", "/appointments/<int:id>")
api.add_resource(BillResource, "/bills", "/bills/<int:id>")
# api.add_resource(DiagnosisResource, "/diagnoses", "/diagnoses/<int:id>")
# api.add_resource(PrescriptionsResource, "/prescriptions", "/prescriptions/<int:id>")
