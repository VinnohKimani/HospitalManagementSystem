from flask_restful import Resource


class DiagnosisResource(Resource):
    def get(self, id=None):
        if id == "None":
            return []
        else:
            return []

    def post(self):
        return {"message": "Diagnosis Created"}

    def patch(self, id):
        return {"message": "Diagnosis Updated"}

    def delete(self, id):
        return {"message": "Diagnosis Deleted"}
