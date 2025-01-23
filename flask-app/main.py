from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

@app.route('/')
def courses():
    # courses = Course.query.all()
    # return render_template('courses.html', courses=courses)
    return render_template('courses.html')

@app.route('/courses-json')
def courses_json():
    courses = Course.query.all()
    courses_list = []
    for course in courses:
        courses_list.append({
            'id': course.id,
            'name': course.name,
            'description': course.description,
            'credits': course.credits
        })
    return jsonify(courses_list)

@app.route('/delete-course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'}), 200
    else:
        return jsonify({'error': 'Course not found'}), 404

@app.route('/add-course', methods=['POST'])
def add_course():
    data = request.get_json()
    new_course = Course(
        name=data['title'],
        description=data['description'],
        credits=data['credits']
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course added successfully'}), 201
# def get_courses():
#     url = 'https://nvyiwigoczwfthfiqojv.supabase.co/rest/v1/Courses?select=*'
#     headers = {
#         'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52eWl3aWdvY3p3ZnRoZmlxb2p2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1Njc0MzEsImV4cCI6MjA1MzE0MzQzMX0.wt0XqdPlmoB7NY0M3KxDS86ZvYWTWkjnfTlgqqfIyjs'
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {'error': 'Failed to retrieve courses'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Course.query.first():
            dummy_courses = [
            Course(name='Introduction to Python', description='Learn the basics of Python programming.', credits=3),
            Course(name='Data Structures', description='Understand various data structures and their applications.', credits=4),
            Course(name='Web Development', description='Build dynamic websites using Flask and other web technologies.', credits=3),
            Course(name='Database Systems', description='Learn about relational databases and SQL.', credits=3)
            ]
            db.session.bulk_save_objects(dummy_courses)
            db.session.commit()
    app.run(host='0.0.0.0', port=5000)