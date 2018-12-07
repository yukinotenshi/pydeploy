import os
import json
import unittest
from boddle import boddle
from pydeploy.util import generate_random_string
from pydeploy.webhook import deploy
from pydeploy.command_chain import CommandChain


class TestWebhook(unittest.TestCase):
    def setUp(self):
        data = {
            'post_script': [],
            'pre_script': [],
            'remote': 'origin',
            'branch': 'master'
        }

        with open("test.json", 'w') as f:
            json.dump(data, f)
        CommandChain.load_from_config("test.json")
        os.remove("test.json")

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
        with boddle(json=payload):
            self.assertEqual(deploy(), expected)
