from pydeploy.notifier.base import Notifier
import requests


class DiscordNotifier(Notifier):
    def send(self, message):
        try:
            r = requests.post(self.receiver, json={"content": message})
        except:
            return False
        return r.status_code == 200
