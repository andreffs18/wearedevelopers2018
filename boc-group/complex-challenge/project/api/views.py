# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint, Response, current_app as app
api_blueprint = Blueprint('api', __name__)

from boc import Client


@api_blueprint.route('/api/v1/locations')
def get_locations():
    c = Client(app.config.get('DEVELOPER_ID'))
    locations = c.get_locations()
    return Response(json.dumps({'locations': locations}), status=200)


@api_blueprint.route('/api/v1/locations/<location_id>')
def get_location_details(location_id):
    c = Client(app.config.get('DEVELOPER_ID'))
    location = c.get_location_details(location_id)
    return Response(json.dumps({'location': location}), status=200)


@api_blueprint.route('/api/v1/servers')
def get_servers():
    c = Client(app.config.get('DEVELOPER_ID'))
    servers = c.get_servers()
    return Response(json.dumps({'servers': servers}), status=200)


@api_blueprint.route('/api/v1/servers/<server_id>')
def get_server_details(server_id):
    c = Client(app.config.get('DEVELOPER_ID'))
    server = c.get_server_details(server_id)
    return Response(json.dumps({'server': server}), status=200)


@api_blueprint.route('/api/v1/applications')
def get_applications():
    c = Client(app.config.get('DEVELOPER_ID'))
    applications = c.get_applications()
    return Response(json.dumps({'applications': applications}), status=200)


@api_blueprint.route('/api/v1/applications/<application_id>')
def get_applications_details(application_id):
    c = Client(app.config.get('DEVELOPER_ID'))
    application = c.get_application_details(application_id)
    return Response(json.dumps({'application': application}), status=200)


