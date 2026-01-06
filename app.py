from flask_migrate import Migrate
from flask import Flask, jsonify, request
from model import db, Mentor, Cohort, Student, MentorCohort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/mentors', methods=['POST'])
def create_mentor():
    data = request.get_json()
    mentor = Mentor(name=data['name'])
    db.session.add(mentor)
    db.session.commit()
    return jsonify({"message": f"Mentor {mentor.name} created"}), 201


@app.route('/cohorts', methods=['POST'])
def create_cohort():
    data = request.get_json()
    cohort = Cohort(name=data['name'])
    db.session.add(cohort)
    db.session.commit()
    return jsonify({"message": f"Cohort {cohort.name} created"}), 201



@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(name=data['name'], cohort_id=data['cohort_id'])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": f"Student {student.name} added to cohort {student.cohort_id}"}), 201


@app.route('/mentor_cohort', methods=['POST'])
def create_mentor_cohort():
    data = request.get_json()
    mentor_id = data['mentor_id']
    cohort_id = data['cohort_id']

    existing = MentorCohort.query.filter_by(mentor_id=mentor_id, cohort_id=cohort_id).first()
    if existing:
        return jsonify({"message": "Mentor already assigned to this cohort"}), 400

    link = MentorCohort(mentor_id=mentor_id, cohort_id=cohort_id)
    db.session.add(link)
    db.session.commit()
    return jsonify({"message": f"Mentor {mentor_id} assigned to Cohort {cohort_id}"}), 201


@app.route('/mentors', methods=['GET'])
def get_top_mentors():
    # Get all mentors from the database
    all_mentors = Mentor.query.all()

    mentor_list = []

    for mentor in all_mentors:
        total_students = 0
        for link in mentor.mentor_cohorts:
            cohort = link.cohort
            total_students += len(cohort.students)

        mentor_info = {
            "mentor_id": mentor.id,
            "mentor_name": mentor.name,
            "total_students": total_students
        }
        mentor_list.append(mentor_info)

    # Function to get total_students from a mentor dictionary
    def get_total_students(mentor):
        return mentor["total_students"]

    mentor_list.sort(key=get_total_students, reverse=True)

    top_5_mentors = mentor_list[:5]

    return jsonify(top_5_mentors)


if __name__ == '__main__':
    app.run(debug=True)