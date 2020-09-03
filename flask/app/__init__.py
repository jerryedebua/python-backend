from flask import Flask

App = Flask(__name__)

from app import routes

# print('Module run as', __name__)
