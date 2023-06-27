"""Database models structure in ORM."""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


class User(db.Model, UserMixin):
    """User db model."""

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    books = db.relationship('Book', backref='published_by', lazy='dynamic')

    def set_password(self, password):
        """Set password hash method."""
        set_password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password hash method."""
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        """Format representation of data in class when printed. Used in debug."""
        return '<User {}>'.format(self.username)


class Book(db.Model):
    """Book model."""

    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    book_author = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.userid'))

    def __repr__(self):
        """Class representation when printing."""
        return '<Book {}>'.format(self.book_name)


@login.user_loader
def load_user(user_id):
    """Get user id from database for user loader."""
    return User.query.get(int(user_id))
