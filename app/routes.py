from flask_login.utils import logout_user
from app import app, db
from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.forms import RegistrationForm, LoginForm


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', user=current_user)


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    return render_template('settings.html', user=current_user, title='Settings')


@app.get('/register')
@app.post('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.online = True
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=False)
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')


@app.get('/login')
@app.post('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title='Login')


@app.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.get('/api/users')
def defaultUsers():
    users = []
    for user in User.query.all():
        users.append({
            "id": user.id,
            "username": user.username,
            "online": user.online,
            "age": user.age,
            "location": user.location,
            "work_related": user.work_related,
            "about_me": user.about_me,
            "hobbies": user.hobbies,
            "paramaters": user.paramaters,
            "profile_image": user.profile_image, #! Links
            "background_image": user.background_image, #! Delete
            "facebook": user.facebook,
            "twitter": user.twitter,
            "youtube": user.youtube,
            "spotify": user.spotify
            })

    return jsonify(users)


@app.get('/api/users/<paramaters>')
def filteredByParamaters(paramaters):
    users = []
    users_dic = {}
    final_users = []
    paramaters = paramaters.split('+')
    

    # determines who should be displayed first based on a ranking system
    # ranking system = most matching paramaters - descending
    for paramater in paramaters:
        for i in User.query.filter(User.paramaters.contains(paramater)):
            users.append(i.username)
    for user in users:
        users_dic.update({user : users.count(user)})

    sort_users = sorted(users_dic.items(), key=lambda x: x[1], reverse=True)

    # Prepares and returns a json with user objects
    for user in sort_users:
        user_model = User.query.filter_by(username=user[0]).first()
        user_obj = {
            "id": user_model.id,
            "username": user_model.username,
            "online": user_model.online,
            "age": user_model.age,
            "location": user_model.location,
            "work_related": user_model.work_related,
            "about_me": user_model.about_me,
            "hobbies": user_model.hobbies,
            "paramaters": user_model.paramaters,
            "profile_image": user_model.profile_image, #! Links
            "background_image": user_model.background_image, #! Links
            "facebook": user_model.facebook,
            "twitter": user_model.twitter,
            "youtube": user_model.youtube,
            "spotify": user_model.spotify
            }
        final_users.append(user_obj)

    return jsonify(final_users)


