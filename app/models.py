"""Database models structure in ORM."""

from app import db


class User(db.Model):
    """User db model."""

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    books = db.relationship('Book', backref='published_by', lazy='dynamic')

    def __repr__(self):
        """Format representation of data in class when printed. Used in debug."""
        return '<User {}>'.format(self.username)


class Book(db.Model):
    """Book model."""

    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    book_author = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.userid'))
