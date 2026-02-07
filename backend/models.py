from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owner = db.Column(db.String(80), nullable=False)
    medical_card_id = db.Column(db.Integer, db.ForeignKey('medical_cards.id'), unique=True)

    medical_card = db.relationship(
        'MedicalCard',
        back_populates='patient',
        uselist=False,
        cascade='all, delete-orphan',
        single_parent=True,
        foreign_keys=[medical_card_id]
    )

class Doctor(db.Model):

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(80), nullable=False)

class Appointment(db.Model):

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    patient = db.relationship(
        'Patient',
        uselist=False,
        foreign_keys=[patient_id]
    )
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    doctor = db.relationship(
        'Doctor',
        uselist=False,
        foreign_keys=[doctor_id]
    )
    date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(255), nullable=False)


class MedicalCard(db.Model):
    __tablename__ = 'medical_cards'

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    patient = db.relationship(
        'Patient',
        back_populates='medical_card',
        uselist=False
    )
