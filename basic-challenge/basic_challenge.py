import os
import logging

from requests import request
from requests.auth import HTTPBasicAuth

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Client:

    BASE_API_URL = "https://wad-challenge-2018.boc-cloud.com/rest/dev"

    def __init__(self, developer_id=None, username="WeAreDevelopers", password="YesWeAre"):
        self.developer_id = developer_id
        self.username = username
        self.password = password
        self.auth = HTTPBasicAuth(self.username, self.password)

        if not self.developer_id:
            raise ValueError("Developer ID is required!")

    def get_model_image(self, filename="model.jpg"):
        """
        Download Image for basic challenge and save content on file with given filename
        """
        url = self.BASE_API_URL + "/models/{}".format(self.developer_id)
        response = request("GET", url, auth=self.auth)
        if response.status_code != 200:
            logger.error("Error {}: \"Failed to fetch image from {} ({})\"".format(response.status_code, url,
                                                                                   response.text))
            return False

        logger.debug("Got {}.".format(response.status_code))
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "wb") as new_img:
            new_img.write(response.content)

        logger.debug("Created {}!".format(filepath))

    def send_code_number(self, code_number):
        """
        Post given code number
        """
        url = self.BASE_API_URL + "/developers/{}/codes".format(self.developer_id)
        params = {'code': code_number}
        response = request("POST", url, data=params, auth=self.auth)
        if response.status_code != 200:
            logger.error("Error {}: \"Failed to post code onto {} ({})\"".format(response.status_code, url,
                                                                                 response.text))
            return None

        logger.info("{}".format(code_number, response.text))
