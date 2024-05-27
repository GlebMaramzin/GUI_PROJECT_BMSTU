from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin_timetable:cde#4rfv@localhost:5432/timetabledb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Students(db.Model):
    studbilet = db.Column(db.String(10), primary_key=True)
    fio = db.Column(db.String(200), primary_key=True)
    grupa = db.Column(db.String(16))
    facult = db.Column(db.String(10))


class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_title = db.Column(db.String(16))
    day_week = db.Column(db.String(12))
    lesson_time = db.Column(db.String(6))
    lesson_type = db.Column(db.String(12))
    lesson_title = db.Column(db.String(200))
    cabinet = db.Column(db.String(30))
    teacher = db.Column(db.String(200))
    week_type = db.Column(db.String(1))


class SearchForm(FlaskForm):
    searched = StringField("Searched")
    submit = SubmitField("Submit")


@app.route('/search')
def search():
    q = request.args.get('q')
    if q:
        s = Students.query.filter(Students.fio.contains(q) |
                                  Students.studbilet.contains(q) |
                                  Students.grupa.contains(q)).all()
    else:
        s = []
    return render_template('search.html', studs=s)


@app.route('/timetable')
def timetable():
    q2 = request.args.get('q2')
    s_day = request.args.get('day_select')
    s_time = request.args.get('time_select')
    lssn = request.args.get('lssn_name')
    if lssn: #distinct(Timetable.group_title)
        ts = Timetable.query.filter(Timetable.lesson_title.contains(lssn) &
                                    Timetable.lesson_time.contains(s_time) &
                                    Timetable.day_week.contains(s_day) ).all()
    else:
        ts = []
    return render_template('timetable.html', ts=ts)

@app.route('/timetable_2')
def timetable2():
    q2 = request.args.get('q2')
    s_day = request.args.get('day_select')
    s_time = request.args.get('time_select')
    lssn = request.args.get('lssn_name')
    if lssn: #distinct(Timetable.group_title)
        ts = Timetable.query.filter(Timetable.lesson_title.contains(lssn) &
                                    Timetable.lesson_time.contains(s_time) &
                                    Timetable.day_week.contains(s_day)).all()
    else:
        ts = []
    return render_template('timetable2.html', ts=ts)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def loging():
    message = ''
    if request.method == 'GET':
        return render_template('base.html')
    else:
        return render_template('login.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/about')
def about_us():
    return render_template('about.html')


if __name__ == 'main':
    app.run(debug=True)