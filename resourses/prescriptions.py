from flask_restful import Resource

class Prescriptions(Resource):
    def get(self, id=None):
        if id == "None":
            return []
        else:
            return []

    def post(self):
        return {"message": "Prescriptions Created"}

    def patch(self, id):
        return {"message": "Prescriptions Updated"}

    def delete(self, id):
        return {"message": "Prescriptions Deleted"}
