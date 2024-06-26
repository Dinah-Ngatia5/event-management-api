from flask import Blueprint, request, jsonify, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from .extensions import db, bcrypt
from .utils import validate_register_form, validate_login_form

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.profile'))

        flash('Invalid credentials. Please try again.')

    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if request.is_json:
            data = request.json
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
        else:
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

        if not username or not email or not password:
            if request.is_json:
                return jsonify({"error": "Missing data"}), 400
            flash('Missing data. Please try again.')
            return redirect(url_for('auth.signup'))

        if not validate_register_form(username, email, password):
            if request.is_json:
                return jsonify({"error": "Invalid form data"}), 400
            flash('Invalid form data. Please try again.')
            return redirect(url_for('auth.signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email)
        new_user.password_hash = hashed_password  

        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            if request.is_json:
                return jsonify({"message": "User created successfully"}), 201
            return redirect(url_for('main.profile'))
        except Exception as e:
            db.session.rollback()
            if request.is_json:
                return jsonify({"error": str(e)}), 500
            flash('An error occurred. Please try again.')
            return redirect(url_for('auth.signup'))

    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
