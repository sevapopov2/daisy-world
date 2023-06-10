"""Routes, same as url confs in Django."""


from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    """Index view."""
    user = {'username': 'Всеволод'}
    return render_template('index.html', title='Главная Страница', user=user)
