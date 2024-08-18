from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def transfer_money_to_card(self, amount: float):
        pass

    @abstractmethod
    def retrieve_money_from_card(self, amount: float):
        pass


class CreditCard(Card):
    def __init__(self) -> None:
        self.percentage = 5
        self.amount_of_money = 0

    def transfer_money_to_card(self, amount: float):
        self.amount_of_money += amount

    def retrieve_money_from_card(self, amount: float):
        self.amount_of_money -= amount + amount * self.percentage / 100
        