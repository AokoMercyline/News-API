# Initializing application
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__,instance_relative_config = True)
import requests
# Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)