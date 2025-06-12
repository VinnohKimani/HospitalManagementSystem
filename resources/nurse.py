from flask_restful import Resource
from models.nurse import Nurse


class NurseResource(Resource):
    def get(self, id=None):
        if id == None:
            nurses = Nurse.query.all()
            return nurses
        else:
            nurse = Nurse.query.filter_by(id=id).first()
            return nurse

    def post(self):
        return {"message": "Nurse Created"}

    def patch(self, id):
        return {"message": "Nurse Updated"}

    def delete(self, id):
        return {"message": "Nurse Deleted"}
