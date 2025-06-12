from flask_restful import Resource

class DoctorResource(Resource):
    def  get(self,id = None):
        if id == "None":
            return []
        else:
            return []
        
    def post(self):
        return {"message": "Doctor Created"}

    def patch(self, id):
        return {"message": "Doctor Updated"}

    def delete(self, id):
        return {"message": "Doctor Deleted"}
 