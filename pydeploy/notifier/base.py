class Notifier:
    def __init__(self, receiver):
        self.receiver = receiver

    def send(self, message):
        raise NotImplementedError()
