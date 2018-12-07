import subprocess


class Command:
    def __init__(self, cmd_str):
        self.cmd = cmd_str
        self.out = ""

    def execute(self):
        try:
            process = subprocess.run(self.cmd, shell=True, stdout=subprocess.PIPE)
            self.out = str(process.stdout)
        except AttributeError:
            command = self.cmd.split()
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
            self.out, _ = process.communicate()
        return process.returncode == 0
