import unittest
from pydeploy.notifier import DiscordNotifier, SlackNotifier, Notifier
from pydeploy.util import generate_random_string


class TestNotifier(unittest.TestCase):
    def test_receiver_must_equal(self):
        expected = generate_random_string()
        discord = DiscordNotifier(expected)
        slack = SlackNotifier(expected)
        base = Notifier(expected)

        self.assertEqual(discord.receiver, slack.receiver)
        self.assertEqual(slack.receiver, base.receiver)

    def test_must_fail_silently(self):
        fake_host = "http://localhost:99999"
        discord = DiscordNotifier(fake_host)
        slack = SlackNotifier(fake_host)

        self.assertFalse(slack.send(''))
        self.assertFalse(discord.send(''))
