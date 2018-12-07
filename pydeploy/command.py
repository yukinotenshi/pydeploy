import subprocess


class Command:
    def __init__(self, cmd_str):
        self.cmd = cmd_str
        self.out = ""
        self.err = ""

    def execute(self):
        try:
            process = subprocess.run(
                self.cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            self.out = str(process.stdout)
            self.err = str(process.stderr)
        except AttributeError:
            command = self.cmd.split()
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = process.communicate()
            self.out, self.err = str(out), str(err)
        return process.returncode == 0
