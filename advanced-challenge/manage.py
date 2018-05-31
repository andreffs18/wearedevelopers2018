# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask_script import Manager
from flask import render_template
from project import create_app

app = create_app()
manager = Manager(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()


__version_ = '1.0.0'
__email__ = "andreffs18@gmail.com"
