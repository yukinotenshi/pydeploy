from pydeploy.notifier.base import Notifier
import requests


class SlackNotifier(Notifier):
    def send(self, message):
        try:
            r = requests.post(self.receiver, json={"text": message})
        except:
            return False
        return r.status_code == 200
