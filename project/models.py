from project import db
from datetime import date, time

class Intern(db.Model):
    
    __tablename__ = 'intern'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    duration = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    int_date = db.Column(db.Date, unique=True, nullable=False)
    int_time = db.Column(db.Time, unique=True, nullable=False)

    def __init__(self, name, school, department, phone, duration, email, message, int_date, int_time):
        self.name = name
        self.school = school
        self.department = department
        self.phone = phone
        self.email_confirmed = False
        self.duration = duration
        self.email = email
        self.message = message
        self.int_time = int_time
        self.int_date = int_date

    def __repr__(self):
        return '<title {}'.format(self.name)