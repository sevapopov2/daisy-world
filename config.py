"""Configuration file for secret key and other important elements."""

import os


class Config(object):
    """Class that stores secret key and other configuration."""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
