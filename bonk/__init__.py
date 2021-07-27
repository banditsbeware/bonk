import os

from flask import Flask

# "application factory function"
def create_app(test_config=None):

    # create and configure application
    app = Flask(__name__, template_folder='scaff', instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    # load configuration, if given
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensire that instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import routes
    app.register_blueprint(routes.router)

    return app
