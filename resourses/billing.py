from flask_restful import Resource


class BillResource(Resource):
    def get(self, id=None):
        if id == "None":
            return []
        else:
            return []

    def post(self):
        return {"message": "Bill Created"}

    def patch(self, id):
        return {"message": "Bill Updated"}

    def delete(self, id):
        return {"message": "Bill Deleted"}
