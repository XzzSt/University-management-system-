# models.py
from extensions import db

class Student(db.Model):
    __tablename__ = 'student'
    uin = db.Column(db.Integer, primary_key=True)
    stuname = db.Column(db.String(30), nullable=False)
    birthyear = db.Column(db.Integer)
    gender = db.Column(db.String(6))
    phone = db.Column(db.Float)
    major = db.Column(db.String(20))

class Study(db.Model):
    __tablename__ = 'study'
    courseid = db.Column(db.String(10), primary_key=True)
    uin = db.Column(db.Integer, db.ForeignKey('student.uin'), primary_key=True)
    score = db.Column(db.Integer, default=None)
    student = db.relationship('Student', backref=db.backref('studies', lazy=True))
    # Add or update this in the Study model
    courseid = db.Column(db.String(10), db.ForeignKey('course.courseid'))


class Professor(db.Model):
    __tablename__ = 'professor'
    profuin = db.Column(db.Integer, primary_key=True)
    profname = db.Column(db.String(30), nullable=False)
    departmentname = db.Column(db.String(30))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(6))

class CourseProfessor(db.Model):
    __tablename__ = 'course_professor'
    courseid = db.Column(db.String(10), primary_key=True)
    profuin = db.Column(db.Integer, db.ForeignKey('professor.profuin'))
    professor = db.relationship('Professor', backref=db.backref('courses', lazy=True))


class Course(db.Model):
    __tablename__ = 'course'
    courseid = db.Column(db.String(10), primary_key=True)
    credit = db.Column(db.Integer)
    crn = db.Column(db.Integer)
    department = db.Column(db.String(30))
    start_date = db.Column(db.Float)  # Consider changing this to db.DateTime if it stores dates
    students = db.relationship('Study', backref='course', lazy=True)

