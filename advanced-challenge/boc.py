import json
import logging

import requests
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Client:

    BASE_API_URL = "https://wad-challenge-2018.boc-cloud.com/rest/dev"

    def __init__(self, developer_id=None, username="WeAreDevelopers", password="YesWeAre"):
        if not developer_id:
            raise ValueError("Developer ID is required!")

        self.developer_id = developer_id
        self.header = {
            'developerId': self.developer_id,
        }

        self.username = username
        self.password = password
        self.auth = HTTPBasicAuth(self.username, self.password)

    def _make_request(self, url):
        response = requests.get(url, auth=self.auth, headers=self.header)
        if response.status_code != 200:
            logger.error("ERROR {}: Failed to return valid response from \"{}\" ({})"
                         "".format(response.status_code, url, response.text))
            return {}
        content = json.loads(response.content)

        if content.get('error'):
            logger.error("ERROR: {}".format(content.get('errString')))
            return {}

        return content

    def get_locations(self):
        url = self.BASE_API_URL + "/locations"
        response = self._make_request(url)
        return response.get('payload')

    def get_servers(self):
        url = self.BASE_API_URL + "/servers"
        response = self._make_request(url)
        return response.get('payload')

    def get_applications(self):
        url = self.BASE_API_URL + "/applications"
        response = self._make_request(url)
        return response.get('payload')

    def get_location_details(self, location_id):
        url = self.BASE_API_URL + "/locations/{}/".format(location_id)
        response = self._make_request(url)
        return response.get('payload')

    def get_server_details(self, server_id):
        url = self.BASE_API_URL + "/servers/{}/".format(server_id)
        response = self._make_request(url)
        return response.get('payload')

    def get_application_details(self, application_id):
        url = self.BASE_API_URL + "/applications/{}/".format(application_id)
        response = self._make_request(url)
        return response.get('payload')