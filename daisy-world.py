"""File to make the app working by importing it."""

from app import app, db
from app.models import User


@app.shell_context_processor
def make_shell_context():
    """Open flask shell with imported db."""
    return {'db': db, 'User': User}
