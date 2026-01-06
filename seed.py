from app import app
from model import db, Mentor, Cohort, Student, MentorCohort

with app.app_context():
    db.drop_all()
    db.create_all()

    m1 = Mentor(name="Alice")
    m2 = Mentor(name="Bob")
    m3 = Mentor(name="Charlie")
    m4 = Mentor(name="Diana")
    m5 = Mentor(name="Eli")
    m6 = Mentor(name="Faith")
    m7 = Mentor(name="Sam")
    m8 = Mentor(name="Beatrice")
    m9 = Mentor(name="Fortune")
    m10 = Mentor(name="Abiud")

    c1 = Cohort(name="Fullstack-c1 2026")
    c2 = Cohort(name="Fullstack-c2 2026")
    c3 = Cohort(name="Fullstack-c3 2026")

    links = [
        MentorCohort(mentor=m1, cohort=c1),
        MentorCohort(mentor=m2, cohort=c1),
        MentorCohort(mentor=m2, cohort=c2),
        MentorCohort(mentor=m3, cohort=c3),
        MentorCohort(mentor=m4, cohort=c2),
        MentorCohort(mentor=m5, cohort=c3),
        MentorCohort(mentor=m6, cohort=c1)
    ]

    students = [
        Student(name="John", cohort=c1),
        Student(name="Mary", cohort=c1),
        Student(name="Grace", cohort=c2),
        Student(name="Kevin", cohort=c2),
        Student(name="Anna", cohort=c3),
        Student(name="Paul", cohort=c3),
        Student(name="Nina", cohort=c2),
        Student(name="Joyce", cohort=c3),
        Student(name="Mercy", cohort=c1),
        Student(name="John", cohort=c3),
        Student(name="Kevin", cohort=c1),
        Student(name="Nelly", cohort=c3),
        Student(name="Natalie", cohort=c2),
        Student(name="Ian", cohort=c3),
        Student(name="Nanjira", cohort=c2),
        Student(name="Verah", cohort=c3),
        Student(name="Emmy", cohort=c1),

    ]

    db.session.add_all([m1, m2, m3, m4, m5, m6,m7,m8,m9,m10, c1, c2, c3] + links + students)
    db.session.commit()

    print(" Database seeded successfully!")