# from flask import Flask, url_for
# import os
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from instance.config import DevConfig
# app = Flask(__name__)
# app.config.from_object(DevConfig)
# db = SQLAlchemy(app)
# Migrate(app, db)
# from newsproject import views
# from newsproject.news_article.views import news_article_blueprint
# from newsproject.news_source.views import news_source_blueprint
# app.register_blueprint(news_article_blueprint, url_prefix='/articles')
# app.register_blueprint(news_source_blueprint, url_prefix='/news_source')
# # @news_source_blueprint.route('/category>')


















# # Initializing application
# from flask import Flask
# from flask_bootstrap import Bootstrap

# app = Flask(__name__,instance_relative_config = True)
# import requests
# # Setting up configuration
# # app.config.from_object(DevConfig)
# # app.config.from_pyfile("config.py")

# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)