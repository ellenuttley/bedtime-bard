"""
This file contains the initialisation of our app; including the app itself, the database, the login manager and the
routes blueprint.

Also contains the function to insert the initial data into the database - please do this before you run for the first
time but then immediately comment it out, or you will end up with duplicated data in the forms.
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
import os
from os import environ, path
basedir = path.abspath(path.dirname(__file__))

login_manager = LoginManager()                                            # defines the login manager

db = SQLAlchemy()                                                         # defines the database


def create_app():                                                         # function to generate the app
    app = Flask(__name__, instance_relative_config=False)                 # defines the core application


    # configures the database :
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'bedtimebard.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'bedtime-bard'
    db.init_app(app)

    login_manager.init_app(app)                                           # registers the login manager for flask-login
    login_manager.login_view = 'routes.login'                             # and sets the route where people login

    from .routes import routes_bp
    app.register_blueprint(routes_bp)                                     # registers the routes blueprint
    
    from . import models

    with app.app_context():
        from . import routes  # Import routes
        from .initial_data import insert_initial_data   #
        bootstrap = Bootstrap5(app)
        db.create_all()  # Create database tables from our models

# ----------- PLEASE UN-COMMENT BEFORE RUNNING FOR THE FIRST TIME ---------------------------------------------------
        # insert_initial_data()   # inserts initial data to the database - for the forms etc.
# ----------------------------------------------------------------------------------------------------------------------

        @app.errorhandler(404)
        def page_not_found(e):
            return render_template('404.html'), 404

        return app


if __name__ == "__main__":
    app.run(debug=True)

