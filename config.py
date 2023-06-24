"""Configuration file for secret key and other important elements."""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Class that stores secret key and other configuration."""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'daisy_world.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
