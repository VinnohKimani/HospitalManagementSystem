from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from Models import db


app = Flask(__name__)
# Cofiguring flask app using config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospitalManagementSystem.db"
app.config["SQLALCHEMY_ECHO"] = True

# Links db to flask app
db.init_app(app)

# import models
from Models.doctors import Doctor
from Models.patient import Patients
from Models.nurse import Nurse
from Models.prescription import Prescriptions
from Models.diagnosis import Diagnosis
from Models.appointment import *
from Models.billing import *

# import resources
from resourses.doctors import DoctorResource
from resourses.patient import PatientResource
from resourses.nurse import NurseResource
from resourses.appointment import AppointmentResource
from resourses.billing import BillResource
from resourses.diagnosis import DiagnosisResource
from resourses.prescriptions import PrescriptionsResource


# Linking flask resfull with app
api = Api(app)

# create migrations
migrate = Migrate(app, db)


# Routes
@app.route("/")
def index():
    return {"message": "Welcome to our hospital API"}


api.add_resource(DoctorResource, "/doctors", "/doctors/<int:doctor_id>")
api.add_resource(PatientResource, "/patients", "/patients/<int:id>")
api.add_resource(NurseResource, "/nurses", "/nurses/<int:id>")
api.add_resource(AppointmentResource, "/appointments", "/appointments/<int:id>")
api.add_resource(BillResource, "/bills", "/bills/<int:id>")
api.add_resource(DiagnosisResource, "/diagnoses", "/diagnoses/<int:id>")
api.add_resource(PrescriptionsResource, "/prescriptions", "/prescriptions/<int:id>")
