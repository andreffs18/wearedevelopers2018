# !/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')

    # define logging patterns
    formatter = logging.Formatter("[%(asctime)s] %(funcName)s:%(lineno)d %(levelname)s - %(message)s")
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    # remove default Flask debug handler
    del app.logger.handlers[0]

    # register view blueprints
    from project.home.views import app_blueprint
    app.register_blueprint(app_blueprint)

    from project.api.views import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
