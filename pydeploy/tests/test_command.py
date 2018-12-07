import unittest
from pydeploy.util import generate_random_string
from pydeploy.command import Command


class TestCommand(unittest.TestCase):
    def test_command(self):
        random_str = generate_random_string()
        cmd = Command("echo " + random_str)
        result = cmd.execute()
        self.assertTrue(result)
        self.assertIn(random_str, cmd.out)
