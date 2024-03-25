from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import Student, Study, CourseProfessor,Professor, Course


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xzz001101@localhost/Database for project 1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Good_Luck_2024'
db.init_app(app)



@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        try:
            new_student = Student(
                uin=request.form.get('uin'),
                stuname=request.form.get('name'),
                birthyear=request.form.get('birth_year'),
                gender=request.form.get('gender'),
                phone=request.form.get('phone'),
                major=request.form.get('major')
            )
            db.session.add(new_student)
            db.session.commit()
            flash('Student successfully added!')
        except Exception as e:
            db.session.rollback()
            flash('Error: ' + str(e))
        return redirect(url_for('add_student'))  # Redirect to the same page as an example

    return render_template('add_student.html')


@app.route('/search_scores', methods=['GET', 'POST'])
def search_scores():
    if request.method == 'POST':
        uin = request.form['uin']
        course_id = request.form['course_id']  # Assume there's a field for course_id in your form
        student_scores = Study.query.filter_by(uin=uin, courseid=course_id).all()
        return render_template('search_results.html', student_scores=student_scores)

    return render_template('search_scores.html')

@app.route('/search_course', methods=['GET', 'POST'])
def search_course():
    if request.method == 'POST':
        course_id = request.form.get('course_id')
        course_professor = CourseProfessor.query.filter_by(courseid=course_id).first()
        if course_professor:
            professor = Professor.query.get(course_professor.profuin)
            return render_template('professor_info.html', professor=professor)
        else:
            flash('No professor found for this course ID', 'error')
            return redirect(url_for('search_course'))
    return render_template('search_course.html')

@app.route('/add_professor', methods=['GET', 'POST'])
def add_professor():
    if request.method == 'POST':
        try:
            new_professor = Professor(
                profuin=request.form.get('prof_uin'),  # Adjusted from prof_uin to profuin
                profname=request.form.get('prof_name'),  # Adjusted from prof_name to profname
                departmentname=request.form.get('department_name'),  # This remains unchanged
                age=request.form.get('age'),  # This remains unchanged
                gender=request.form.get('gender')  # This remains unchanged
            )
            db.session.add(new_professor)
            db.session.commit()
            flash('Professor successfully added!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error: ' + str(e), 'error')
        return redirect(url_for('add_professor'))

    return render_template('add_professor.html')

@app.route('/search_course_info', methods=['GET', 'POST'])
def search_course_info():
    if request.method == 'POST':
        course_id = request.form.get('course_id')
        course = Course.query.filter_by(courseid=course_id).first()
        if course:
            return render_template('course_info.html', course=course)
        else:
            flash('No course found with this Course ID.', 'error')
            return redirect(url_for('search_course_info'))

    return render_template('search_course_info.html')


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables for our data models
    app.run(debug=True)
