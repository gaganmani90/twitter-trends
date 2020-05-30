import urllib

from flask import Flask
from flask_testing import TestCase


class MyTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        # Set to 0 to have the OS pick the port.
        app.config['LIVESERVER_PORT'] = 0
        return app

    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    @staticmethod
    def get_server_url():
        return "http://localhost:5000"


