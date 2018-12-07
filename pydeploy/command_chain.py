class CommandChain:
    def __init__(self):
        self.commands = []

    @classmethod
    def load_from_config(cls):
        pass

    def add_command(self, cmd_str):
        pass

    def execute(self):
        for c in self.commands:
            c.execute()
