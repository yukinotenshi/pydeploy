import unittest
from boddle import boddle
from pydeploy.util import generate_random_string
from pydeploy.webhook import deploy


class TestWebhook(unittest.TestCase):
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
