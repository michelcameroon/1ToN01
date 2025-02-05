from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    presences = db.relationship('Presence', backref='student', lazy=True)

    def __repr__(self):
        return f'<Student {self.name}>'

class Presence(db.Model):
    __tablename__ = 'presence'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __repr__(self):
        return f'<Presence {self.date} - {self.status}>'
