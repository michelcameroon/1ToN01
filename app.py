from flask import Flask, render_template, request, redirect, url_for
from models import db, Student, Presence
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#@app.before_first_request
@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form.get('name')
    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_presence/<int:student_id>', methods=['POST'])
def add_presence(student_id):
    date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
    status = request.form.get('status')
    new_presence = Presence(date=date, status=status, student_id=student_id)
    db.session.add(new_presence)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
