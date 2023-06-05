"""File for initializing app's package."""

from flask import Flask

app = Flask(__name__)

from app import routes
