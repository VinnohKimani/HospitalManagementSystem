# ASSIGNMENT

- Come up with an Idea and  3 to 5 models (account for relationships)
- Create the complete routes for each model (C.R.U.D)
- Create a postman collection of all models for those routes
- Refactor the flask routes and use flask-restful

# Idea
- Hospital Managemnt System

# Entities
- Doctor(Vincent)
- Patient(Ruth)
- Nurse(Elfas)
- Billing(Johnson)
- Diagnosis(Vincent)
- Prescription(Ruth)
- Appointment(Johnson)

# Attributes 
- Doctor(id, name, specialization)
- Patient(id, full_name, diagnosis_id, created_at, updated_at, deleted_at, doctor_id)
- Nurse (id, name)
- Billing(id, amount, diagnosis_id, created_at, updated_at, deleted_at)
- Prescription(id, patient_id, doctor_id, diagnosis_id, created_at, updated_at,deleted_at )
- Diagnosis(id, diagonis_note)
- Appointment(id, created_at, deleted_at, patient_id, doctor_id)
      
# Relationship
- Doctor and Patient (One to many) ---->(Association Technique(One to many))
- Patient and Billing (One to many)
- Nurse and Patient (Many to many)
- Patient and Prescription (One to One)
- Patient and Appointment (One to many)
- Patient and Diagnosis (One to many)--->(Aggregation Technique (One to many relationship))


# Things To Confirm 
- Relationship between Doctor and Patient (Is nurse an intemidiary class) making the       relationship many to many

      
       
   