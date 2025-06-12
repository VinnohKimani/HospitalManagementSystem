from flask_restful import Resource
from Models.prescription import Prescriptions


class PrescriptionsResource(Resource):
    def get(self, id=None):
        if id == "None":
            prescs = Prescriptions.query.all()
            return prescs
        else:
            presc = Prescriptions.query.filter_by(id=id).first()
            return presc

    def post(self):
        return {"message": "Prescriptions Created Testing push"}

    def patch(self, id):
        return {"message": "Prescriptions Updated"}

    def delete(self, id):
        return {"message": "Prescriptions Deleted"}
