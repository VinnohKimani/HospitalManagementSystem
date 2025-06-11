from flask import Flask
from flask_restful import Api

from resourses.doctors import DoctorResource
from resourses.patient import PatientResource
from resourses.nurse import NurseResource
from resourses.appointment import AppointmentResource
from resourses.billing import BillResource
from resourses.diagnosis import DiagnosisResource
from resourses.prescriptions import Prescriptions

app = Flask(__name__)

# Cofiguring flask app using config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospitalManagementSystem.db"

# Linking flask resfull with app
api = Api(app)



api.add_resource(DoctorResource, "/doctors", "/doctors/<int:doctor_id>")
api.add_resource(PatientResource, "/patients", "/patients/<int:id>")
api.add_resource(NurseResource, "/nurses", "/nurses/<int:id>")
api.add_resource(AppointmentResource, "/appointments", "/appointments/<int:id>")
api.add_resource(BillResource, "/bills", "/bills/<int:id>")
api.add_resource(DiagnosisResource, "/diagnoses", "/diagnoses/<int:id>")
api.add_resource(Prescriptions, "/prescriptions", "/prescriptions/<int:id>")
