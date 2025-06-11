# from flask import Flask
# from flask_restful import Api
# from resources.doctors import DoctorResource

# app = Flask(__name__)
# api = Api(app)


# # Doctor HTTP Methods
# # # @app.post("/doctors")
# # # def post_doctor():
# # #     return {"message": "Doctor Added Successfully"}


# # # @app.get("/doctors")
# # # def get_doctors():
# # #     return {"message": "patients Retrieved Successfully"}


# # # @app.get("/doctor/<int:id>")
# # # def get_doctor(id):
# # #     return {"message": "Doctor Retrieved Successfully"}


# # # @app.patch("/doctor/<int:id>")
# # # def update_doctor(id):
# # #     return {"message": "Doctor Updated Successfully"}


# # # @app.delete("/doctor/<int:id>")
# # # def delete_doctor(id):
# # #     return {"message": "Doctor Delete Successfully"}


# # # <--------Patient------->
# # @app.post("/patients")
# # def post_patient():
# #     return {"message": "Patient Added Successfully"}


# # @app.get("/patients")
# # def get_patients():
# #     return {"message": "Patients Retrieved Successfully"}


# # @app.get("/patient/<int:id>")
# # def get_patient(id):
# #     return {"message": "Patient Retrieved Successfully"}


# # @app.patch("/patient/<int:id>")
# # def update_patient(id):
# #     return {"message": "Patient Updated Successfully"}


# # @app.delete("/patient/<int:id>")
# # def delete_patient(id):
# #     return {"message": "Patient Delete Successfully"}


# # -------Nurse----->
# @app.post("/nurses")
# def post_nurse():
#     return {"message": "Nurse Added Successfully"}


# @app.get("/nurses")
# def get_nurses():
#     return {"message": "Nurse Retrieved Successfully"}


# @app.get("/nurse/<int:id>")
# def get_nurse(id):
#     return {"message": "Nurse Retrieved Successfully"}


# @app.patch("/nurse/<int:id>")
# def update_nurse(id):
#     return {"message": "Nurse Updated Successfully"}


# @app.delete("/nurse/<int:id>")
# def delete_nurse(id):
#     return {"message": "Nurse Delete Successfully"}


# # <-----Prescription ----->
# @app.post("/prescriptions")
# def post_prescriptions():
#     return {"message": "Prescription Added Successfully"}


# @app.get("/prescriptions")
# def get_prescriptions():
#     return {"message": "Prescription Retrieved Successfully"}


# @app.get("/prescription/<int:id>")
# def get_prescription(id):
#     return {"message": "Prescription Retrieved Successfully"}


# @app.patch("/prescription/<int:id>")
# def update_prescription(id):
#     return {"message": "Prescription Updated Successfully"}


# @app.delete("/prescription/<int:id>")
# def delete_prescription(id):
#     return {"message": "Prescription Delete Successfully"}


# # -------Diagnosis ----->
# @app.post("/diagnoses")
# def post_diagnoses():
#     return {"message": "Diagnosis Added Successfully"}


# @app.get("/diagnoses")
# def get_diagnoses():
#     return {"message": "Diagnosis Retrieved Successfully"}


# @app.get("/diagnosis/<int:id>")
# def get_diagnosis(id):
#     return {"message": "Diagnosis Retrieved Successfully"}


# @app.patch("/diagnosis/<int:id>")
# def update_diagnosis(id):
#     return {"message": "Diagnosis Updated Successfully"}


# @app.delete("/diagnosis/<int:id>")
# def delete_diagnosis(id):
#     return {"message": "Diagnosis Delete Successfully"}


# # <-------Appointment ------>
# @app.post("/appointments")
# def post_appointments():
#     return {"message": "Nurse Added Successfully"}


# @app.get("/appointments")
# def get_appointments():
#     return {"message": "Appointments Retrieved Successfully"}


# @app.get("/appointment/<int:id>")
# def get_appointment(id):
#     return {"message": "Appointment Retrieved Successfully"}


# @app.patch("/appointment/<int:id>")
# def update_appointment(id):
#     return {"message": "Appointment Updated Successfully"}


# @app.delete("/appointment/<int:id>")
# def delete_appointment(id):
#     return {"message": "Appointment Delete Successfully"}


# # <------Billing------>
# @app.post("/bills")
# def post_bills():
#     return {"message": "Bills Added Successfully"}


# @app.get("/bills")
# def get_bills():
#     return {"message": "Bills Retrieved Successfully"}


# @app.get("/bill/<int:id>")
# def get_bill(id):
#     return {"message": "Bill Retrieved Successfully"}


# @app.patch("/bill/<int:id>")
# def update_bill(id):
#     return {"message": "Bill Updated Successfully"}


# @app.delete("/bill/<int:id>")
# def delete_bill(id):
#     return {"message": "Bill Delete Successfully"}



# api.add_resource(DoctorResource, "/doctors", "/doctors/<int:doctor_id>")