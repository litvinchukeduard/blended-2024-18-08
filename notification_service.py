from abc import ABC, abstractmethod

# class NotificationService:
#     def notify(self, id, data, method):
#         if method == 'viber':
#             pass
#         elif method == 'telegram':
#             pass




class Notifier(ABC):
    @abstractmethod
    def send_message(self, id, data: str):
        pass


class ViberNotifier(Notifier):
    def send_message(self, id, data: str):
        print('sending to viber')


class TelegramNotifier(Notifier):
    def send_message(self, id, data: str):
        print('sending to telegram')


class NotificationService:

    def __init__(self) -> None:
        self.notifiers = []

    def notify(self, id, data):
        for notifier in self.notifiers:
            notifier.send_message(id, data)
