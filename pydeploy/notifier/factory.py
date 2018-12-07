from pydeploy.notifier.discord import DiscordNotifier
from pydeploy.notifier.slack import SlackNotifier


class NotifierFactory:
    @staticmethod
    def load(name):
        if name == "slack":
            return SlackNotifier
        elif name == "discord":
            return DiscordNotifier
        else:
            raise ModuleNotFoundError()
