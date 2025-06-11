from flask_restful import Resource


class AppointmentResource(Resource):
    def get(self, id=None):
        if id == "None":
            return []
        else:
            return []

    def post(self):
        return {"message": "Appointment Created"}

    def patch(self, id):
        return {"message": "Appointment Updated"}

    def delete(self, id):
        return {"message": "Appointment Deleted"}
