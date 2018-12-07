import psutil
import subprocess


class Command:
    def __init__(self, cmd_str):
        self.cmd = cmd_str
        self.out = ""
        self.err = ""
        self.process = None

    def execute(self):
        command = self.cmd.split()
        try:
            self.process = subprocess.run(
                self.cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            self.out = str(self.process.stdout)
            self.err = str(self.process.stderr)
        except AttributeError:
            self.process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = self.process.communicate()
            self.out, self.err = str(out), str(err)
        return self.process.returncode == 0

    def kill(self):
        if self.process is None:
            return
        process = psutil.Process(self.process.pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
