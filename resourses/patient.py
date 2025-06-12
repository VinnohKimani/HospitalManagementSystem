from flask_restful import Resource
from Models.patient import Patients


class PatientResource(Resource):
    def get(self, id=None):
        if id == "None":
            patients = Patients.query.all()
            return patients
        else:
            patient = Patients.query.filter_by(id=id).first()
            return patient

    def post(self):
        return {"message": "Paitent Created"}

    def patch(self, id):
        return {"message": "Patient Updated"}

    def delete(self, id):
        return {"message": "Patient Deleted"}
