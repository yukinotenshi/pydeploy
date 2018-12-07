import requests
import unittest
import _thread
import pydeploy.config as config
from pydeploy.util import generate_random_string
config.route = generate_random_string()

from pydeploy.webhook import app


class TestWebhook(unittest.TestCase):
    def setUp(self):
        kwargs = {
            "host": "localhost",
            "port": 9999
        }
        _thread.start_new_thread(app.run, (), kwargs)

    def test_webhook(self):
        payload = {
            "ref": generate_random_string(),
            "pusher": {
                "name": generate_random_string(),
                "email": generate_random_string()
            }
        }
        expected = "{} {} {}".format(
            payload['ref'],
            payload['pusher']['name'],
            payload['pusher']['email'],
        )
        response = requests.post('http://localhost:9999/' + config.route, json=payload)
        self.assertEqual(response.text, expected)
