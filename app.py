from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lineageloom.db'
db = SQLAlchemy(app)


# class User(db.Model):
#     uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nid = db.Column(db.Integer, nullable=False)
#     name = db.Column(db.String(80), nullable=False)
#     birthday = db.Column(db.Date, nullable=False)
#     joined_at = db.Column(db.DateTime, default=datetime.utcnow)


class Person(db.Model):
    nid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(80), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    country = db.Column(db.String(80), nullable=True)
    division = db.Column(db.String(80), nullable=True)
    district = db.Column(db.String(80), nullable=True)
    postal_code = db.Column(db.String(80), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    user = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)



@app.route('/<user>')
def user(user):
    return "Hello " + user + "! Welcome to Lineage Loom."


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_person', methods=['GET', 'POST'])
def createPerson():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        birthday = datetime.strptime(request.form.get('birthday'), '%Y-%m-%d')
        nid = request.form.get('nid')
        gender = request.form.get('gender')
        address = request.form.get('address')
        country = request.form.get('country')
        division = request.form.get('division')
        district = request.form.get('district')
        postal_code = request.form.get('postcode')

        new_person = Person(name=name, phone=phone, birthday=birthday, nid=nid, gender=gender, address=address, country=country, division=division, district=district, postal_code=postal_code)
        db.session.add(new_person)
        db.session.commit()

        return redirect(url_for('database'))

    return render_template('registration.html')


@app.route('/database')
def database():
    persons = Person.query.all()
    return render_template('database.html', persons=persons)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)