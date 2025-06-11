from flask_restful import Resource


class PatientResource(Resource):
    def get(self, id=None):
        if id == "None":
            return []
        else:
            return []

    def post(self):
        return {"message": "Paitent Created"}

    def patch(self, id):
        return {"message": "Patient Updated"}

    def delete(self, id):
        return {"message": "Patient Deleted"}
