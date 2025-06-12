from flask_restful import Resource
from models.doctors import Doctor


class DoctorResource(Resource):
    def get(self, id=None):
        if id == None:
            doctors = Doctor.query.all()
            return doctors
        else:
            doctor = Doctor.query.filter_by(id=id).first()
            return doctor

    def post(self):
        return {"message": "Doctor Created"}

    def patch(self, id):
        return {"message": "Doctor Updated"}

    def delete(self, id):
        return {"message": "Doctor Deleted"}
