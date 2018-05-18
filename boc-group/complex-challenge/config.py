# !/usr/bin/python
# -*- coding: utf-8 -*-
import os


class BaseConfig(object):
    DEBUG = True
    TESTING = False
    MACHINE_NAME = "SANDEEP"
    SECRET_KEY = os.environ.get("SECRET_KEY", "SECRETTZ")
    DEVELOPER_ID = "8978548a-d17a-43a4-8d8c-2da6361b991a"

