import os
import json
import unittest
from pydeploy.util import generate_random_string
from pydeploy.command_chain import CommandChain


class TestCommandChain(unittest.TestCase):
    def setUp(self):
        self.filename = generate_random_string()
        self.first_out = generate_random_string()
        self.second_out = generate_random_string()

    def tearDown(self):
        os.remove(self.filename)
        CommandChain.instance = None

    def test_empty(self):
        data = {
            'pre_script': [],
            'post_script': [],
            'remote': 'origin',
            'branch': 'master'
        }

        with open(self.filename, 'w') as f:
            json.dump(data, f)

        chain = CommandChain.load_from_config(self.filename)
        self.assertEqual(len(chain.commands), 1)
        self.assertEqual(chain.commands[0].cmd, 'git pull origin master')

    def test_prescript_only(self):
        data = {
            'pre_script': [
                "echo " + self.first_out,
                "echo " + self.second_out,
            ],
            'post_script': [],
            'remote': 'origin',
            'branch': 'master'
        }

        with open(self.filename, 'w') as f:
            json.dump(data, f)

        chain = CommandChain.load_from_config(self.filename)
        chain.commands[0].execute()
        chain.commands[1].execute()
        self.assertEqual(len(chain.commands), 3)
        self.assertEqual(chain.commands[2].cmd, 'git pull origin master')
        self.assertIn(self.first_out, chain.commands[0].out)
        self.assertIn(self.second_out, chain.commands[1].out)

    def test_postscript_only(self):
        data = {
            'post_script': [
                "echo " + self.first_out,
                "echo " + self.second_out,
            ],
            'pre_script': [],
            'remote': 'origin',
            'branch': 'master'
        }

        with open(self.filename, 'w') as f:
            json.dump(data, f)

        chain = CommandChain.load_from_config(self.filename)
        chain.commands[1].execute()
        chain.commands[2].execute()
        self.assertEqual(len(chain.commands), 3)
        self.assertEqual(chain.commands[0].cmd, 'git pull origin master')
        self.assertIn(self.first_out, chain.commands[1].out)
        self.assertIn(self.second_out, chain.commands[2].out)

    def test_all(self):
        data = {
            'post_script': [
                "echo " + self.first_out,
                "echo " + self.second_out,
            ],
            'pre_script': [
                "echo " + self.first_out,
                "echo " + self.second_out,
            ],
            'remote': 'origin',
            'branch': 'master'
        }

        with open(self.filename, 'w') as f:
            json.dump(data, f)

        chain = CommandChain.load_from_config(self.filename)
        chain.commands[0].execute()
        chain.commands[1].execute()
        chain.commands[3].execute()
        chain.commands[4].execute()
        self.assertEqual(len(chain.commands), 5)
        self.assertEqual(chain.commands[2].cmd, 'git pull origin master')
        self.assertIn(self.first_out, chain.commands[0].out)
        self.assertIn(self.second_out, chain.commands[1].out)
        self.assertIn(self.first_out, chain.commands[3].out)
        self.assertIn(self.second_out, chain.commands[4].out)
