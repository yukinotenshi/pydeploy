import json
from pydeploy.command import Command
from pydeploy.notifier import NotifierFactory


class CommandChain:
    instance = None

    def __init__(self):
        self.commands = []
        self.notifier = None

    @classmethod
    def load_from_config(cls, file_name):
        if cls.instance is not None:
            return cls.instance

        with open(file_name) as file:
            data = json.load(file)

        cls.instance = cls()
        commands = []
        commands += data['pre_script']
        commands += ['git pull {} {}'.format(data['remote'], data['branch'])]
        commands += data['post_script']
        if 'notifier' in data:
            notifier_class = NotifierFactory.load(data['notifier']['type'])
            cls.instance.notifier = notifier_class(data['notifier']['receiver'])

        for c in commands:
            cls.instance.add_command(c)

        return cls.instance

    def add_command(self, cmd_str):
        self.commands.append(Command(cmd_str))

    def execute(self):
        for c in self.commands:
            executed = c.execute()
            if not executed and self.notifier:
                self.notifier.send(c.out)
