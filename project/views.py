from flask import render_template, request, flash, url_for, redirect, session
from project import app, db
from project.models import Intern
from sqlalchemy import exc
from functools import wraps
from datetime import datetime


def is_registered(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if 'regin' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized access, Please register first', 'error')
            return redirect(url_for('register'))

    return wrapped

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'name' in request.form and 'school' in request.form and 'department' in request.form and 'phone' in request.form and 'duration' in request.form and 'email' in request.form and 'message' in request.form and 'int_date' in request.form and 'int_time' in request.form:
        nw_time =Intern.query.order_by(Intern.int_time, Intern.int_date).all()
        if request.form['int_time'] and request.form['int_date'] != nw_time:

            try:
                new_intern = Intern(name = request.form['name'], school = request.form['school'], department = request.form['department'], phone = request.form['phone'], duration = request.form['duration'], email = request.form['email'], message = request.form['message'], int_date = request.form['int_date'], int_time = request.form['int_time'])
                new_intern.authenticated = True
                db.session.add(new_intern)
                db.session.commit()
                session['regin'] = True
                flash('{} you have been sucessfully registered!'.format(new_intern.name), 'success')
                return redirect(url_for('intern'))
            except exc.IntegrityError:
                db.session.rollback()
                flash('ERROR! Email {} or Time {} already exists.'.format(new_intern.email, new_intern.int_time), 'error')  

    return render_template("index.html", name = "Application")


@app.route('/intern')
@is_registered
def intern():
    users = Intern.query.order_by(Intern.id).all()
    return render_template('intern.html', users=users)
