"""Routes, same as url confs in Django."""


from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    """Index view."""
    user = {'username': 'Всеволод'}
    return render_template('index.html', title='Главная Страница', user=user)


@app.route('/login')
def login():
    """Login view."""
    form = LoginForm()
    return render_template('login.html', title='Вход', form=form)
