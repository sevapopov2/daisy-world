"""Database models structure in ORM."""

from app import db


class User(db.Model):
    """User db model."""

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        """Format representation of data in class when printed. Used in debug."""
        return '<User {}>'.format(self.username)
