"""Database models structure in ORM."""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


class User(db.Model, UserMixin):
    """User db model."""

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def set_password(self, password):
        """Set password hash method."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password hash method."""
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        """Format representation of data in class when printed. Used in debug."""
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(user_id):
    """Get user id from database for user loader."""
    return User.query.get(int(user_id))
