from flask_restful import Resource
from Models.appointment import Appointment


class AppointmentResource(Resource):
    def get(self, id=None):
        if id == "None":
            appointments = Appointment.query.all()
            return appointments
        else:
            appointment = Appointment.query.filter_by(id=id).first()
            return appointment

    def post(self):
        return {"message": "Appointment Created"}

    def patch(self, id):
        return {"message": "Appointment Updated"}

    def delete(self, id):
        return {"message": "Appointment Deleted"}
