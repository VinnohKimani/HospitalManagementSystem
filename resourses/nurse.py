
from flask_restful import Resource


class NurseResource(Resource):
    def get(self, id=None):
        if id == "None":
            return []
        else:
            return []

    def post(self):
        return {"message": "Nurse Created"}

    def patch(self, id):
        return {"message": "Nurse Updated"}

    def delete(self, id):
        return {"message": "Nurse Deleted"}
