'''
Написати систему, яка буде з одної картки переводити гроші на іншу через різні сервіси. 
Переклад за реквізитами, переклад на картку та переклад за гаманцем
'''
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, id, amount):
        pass


class RequisitesProcessor(PaymentProcessor):
    def process_payment(self, id, amount, document=None):
        if document is None:
            raise ValueError
        print('Processing requisites')


class CardProcessor(PaymentProcessor):
    def process_payment(self, id, amount):
        print('Processing card')


class PaymentSystem:
    def __init__(self, payment_processor: PaymentProcessor) -> None:
        self.payment_processor = payment_processor

    def process_payment(self, id, amount):
        self.payment_processor.process_payment(id, amount)


class PaymentSystemTwo:

    def process_payment(self, id, amount, payment_processor):
        if amount < 0:
            raise ValueError
        if len(id) == 0:
            raise ValueError
        payment_processor.process_payment(id, amount)


# class ProcessPayment:

#     def process_payment(self, id, amount, method, document = None):
#         if method == 'requisites':
#             print('Processing requisites')
#         elif method == 'card':
#             print('Processing card')
#         else:
#             print("Processing wallet")


