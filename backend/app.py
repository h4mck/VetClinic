from datetime import date

from flask import Flask, jsonify, request
from flask_cors import CORS
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///clinic.db'
CORS(app)
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()

    return jsonify([
        {
            "id": d.id,
            "name": d.name,
            "age": d.age,
            "sex": d.sex,
        } for d in doctors
    ])

@app.route('/api/doctors', methods=['POST'])
def create_doctor():
    data = request.get_json()

    doctor = Doctor(
        name=data['name'],
        age=data['age'],
        sex=data['sex']
    )

    db.session.add(doctor)
    db.session.commit()

    return jsonify({"id": f"{doctor.id}", "status": "created"}), 201

@app.route('/api/doctors/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    data = request.get_json()

    doctor = Doctor.query.get(doctor_id)
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404

    if 'name' in data:
        doctor.name = data['name']
    if 'age' in data:
        doctor.age = data['age']
    if 'sex' in data:
        doctor.sex = data['sex']

    db.session.commit()

    return jsonify({
        "id": doctor.id,
        "status": "updated"
    }), 200

@app.route('/api/doctors/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404

    db.session.delete(doctor)
    db.session.commit()

    return jsonify({
        "id": doctor.id,
        "status": "deleted"
    }), 200

@app.route('/api/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "owner": p.owner,
            "medical_card_id": p.medical_card_id
        } for p in patients
    ])

@app.route('/api/patients', methods=['POST'])
def create_patient():
    data = request.get_json()

    patient = Patient(
        name=data['name'],
        owner=data['owner'],
    )

    db.session.add(patient)
    db.session.commit()

    return jsonify({"id": f"{patient.id}", "status": "created"}), 201


@app.route('/api/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()

    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    if 'name' in data:
        patient.name = data['name']
    if 'owner' in data:
        patient.owner = data['owner']
    if 'medical_card_id' in data:
        patient.medical_card_id = data['medical_card_id']

    db.session.commit()

    return jsonify({
        "id": patient.id,
        "status": "updated"
    }), 200

@app.route('/api/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()

    return jsonify({
        "id": patient.id,
        "status": "deleted"
    }), 200

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()

    return jsonify([
        {
            "id": a.id,
            "patient_id": a.patient_id,
            "doctor_id": a.doctor_id,
            "date": a.date,
            "reason": a.reason
        } for a in appointments
    ])

@app.route('/api/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()

    patient = Patient.query.get(data['patient'])
    doctor = Doctor.query.get(data['doctor'])

    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404

    got_date = data['date']
    formatted_date = date(int(got_date[6:]), int(got_date[3:5]), int(got_date[0:2]))

    appointment = Appointment(
        patient_id=data['patient'],
        doctor_id=data['doctor'],
        date=formatted_date,
        reason=data['reason']
    )

    db.session.add(appointment)
    db.session.commit()

    return jsonify({"id": f"{appointment.id}", "status": "created"}), 201

@app.route('/api/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    data = request.get_json()

    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    patient = Patient.query.get(data['patient'])
    doctor = Doctor.query.get(data['doctor'])

    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404

    if 'patient' in data:
        appointment.patient_id = data['patient']
    if 'doctor' in data:
        appointment.doctor_id = data['doctor']
    if 'date' in data:
        got_date = data['date']
        formatted_date = date(int(got_date[6:]), int(got_date[3:5]), int(got_date[0:2]))
        appointment.date = formatted_date

    db.session.commit()

    return jsonify({
        "id": appointment.id,
        "status": "updated"
    }), 200

@app.route('/api/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    db.session.delete(appointment)
    db.session.commit()

    return jsonify({
        "id": appointment.id,
        "status": "deleted"
    }), 200

if __name__ == '__main__':
    app.run()
