# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask_dotenv import DotEnv


class BaseConfig(object):
    DEBUG = True
    TESTING = False
    MACHINE_NAME = "Advanced Challenge"
    SECRET_KEY = os.environ.get("SECRET_KEY", "SECRETTZ")
    DEVELOPER_ID = os.environ.get('DEVELOPER_ID', '')

    @classmethod
    def init_app(self, app):
        env = DotEnv()
        env.init_app(app)

