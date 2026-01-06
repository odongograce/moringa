from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class MentorCohort(db.Model):
    __tablename__ = 'mentor_cohort'
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'), nullable=False)
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohorts.id'), nullable=False)

    mentor = db.relationship('Mentor', back_populates='mentor_cohorts')
    cohort = db.relationship('Cohort', back_populates='mentor_cohorts')

    
class Mentor(db.Model):
    __tablename__ = 'mentors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    mentor_cohorts = db.relationship('MentorCohort', back_populates='mentor')

   
class Cohort(db.Model):
    __tablename__ = 'cohorts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)

    mentor_cohorts = db.relationship('MentorCohort', back_populates='cohort')
    students = db.relationship('Student', back_populates='cohort')

    
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohorts.id'), nullable=False)

    cohort = db.relationship('Cohort', back_populates='students')

