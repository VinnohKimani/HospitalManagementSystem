from flask_restful import Resource
from models.diagnosis import Diagnosis


class DiagnosisResource(Resource):
    def get(self, id=None):
        if id == None:
            diagnosis = Diagnosis.query.all()
            return diagnosis
        else:
            diag = Diagnosis.query.filter_by(id=id).first()
            return diag

    def post(self):
        return {"message": "Diagnosis Created"}

    def patch(self, id):
        return {"message": "Diagnosis Updated"}

    def delete(self, id):
        return {"message": "Diagnosis Deleted"}
