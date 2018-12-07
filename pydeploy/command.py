import subprocess


class Command:
    def __init__(self, cmd_str):
        self.cmd = cmd_str
        self.out = ""

    def execute(self):
        process = subprocess.run(self.cmd, shell=True, stdout=subprocess.PIPE)
        self.out = str(process.stdout)
        return process.returncode == 0