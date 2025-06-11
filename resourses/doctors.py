from flask_restful import Resource

class DoctorResource(Resource):
    def  get(self, doctor_id = None):
        if doctor_id == "None":
            return []
        else:
            return []
        
    def post(self):
        return {"message": "Doctor Created"}

    def patch(self, doctor_id):
        return {"message": "Doctor Updated"}

    def delete(self, doctor_id):
        return {"message": "Doctor Deleted"}
 