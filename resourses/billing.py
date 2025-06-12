from flask_restful import Resource
from Models.billing import Billing


class BillResource(Resource):
    def get(self, id=None):
        if id == "None":
            bills = Billing.query.all()
            return bills
        else:
            bill = Billing.query.filter_by(id=id).first()
            return bill

    def post(self):
        return {"message": "Bill Created"}

    def patch(self, id):
        return {"message": "Bill Updated"}

    def delete(self, id):
        return {"message": "Bill Deleted"}
