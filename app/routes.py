"""Routes, same as url confs in Django."""

from app import app


@app.route('/')
@app.route('/index')
def index():
    """Index view."""
    return 'Добро пожаловать в Daisy world!'
