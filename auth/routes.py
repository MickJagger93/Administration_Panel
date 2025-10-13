from flask import Blueprint, render_template, url_for, redirect, flash, get_flashed_messages, request
from flask_login import login_user, logout_user, current_user, login_required
from models import Admin, db
from forms import LoginForm, RegisterForm, ResetForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        admin = Admin.query.filter_by(email=email).first()

        if admin and admin.check_password(password):

            login_user(admin)
            return redirect(url_for('dashboard.dashboard'))

        else:

            flash('User not found or incorrect password. Please try again.')

    return render_template('layouts/partials/login.html', form=form, messages=get_flashed_messages())

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        name = form.name.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:

            flash('Passwords do not match. Please try again.')
            return redirect(url_for('auth.register'))
        
        admin = Admin.query.filter_by(email=email).first()

        if admin:

            flash('Your email is already registered')
            return redirect(url_for('auth.register'))

        else:

            admin = Admin(name=name, email=email, password=password)
            admin.set_password(password)
            db.session.add(admin)
            db.session.commit()

            flash('Successfully registration! Please Log in.')
            return redirect(url_for('auth.login'))
        
    return render_template('layouts/partials/register.html', form=form, messages=get_flashed_messages())

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():

    form = ResetForm()

    if form.validate_on_submit():

        email = form.email.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if new_password == confirm_new_password:

            admin = Admin.query.filter_by(email=email).first()

            if admin:

                admin.set_password(new_password)
                db.session.commit()

                flash('Your password has been successfully updated!')
                return redirect(url_for('auth.login'))

    return render_template('layouts/partials/reset_password.html', form=form, messages=get_flashed_messages())

@auth_bp.route('/logout', methods=['POST'])
def logout():

    logout_user()
    flash('You have been logged out succesfully.')
    return redirect(url_for('index.index'))