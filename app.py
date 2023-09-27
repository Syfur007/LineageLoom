
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lineageloom.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/add', methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         person = Person(name=name, age=age)
#         db.session.add(person)
#         db.session.commit()
#         return redirect(url_for('database'))
#     return render_template('add.html')

# @app.route('/database')

def database():
    persons = Person.query.all()
    return render_template('database.html', persons=persons)

if __name__ == '__main__':
    app.run(debug=True)