from mongoengine import *
from MM2 import ChangeMainBalance

import MM2


class ClientBank(Document):
    Account = StringField()
    Name = StringField()
    Balance = IntField()

    def change(self, amount: int):
        self.Balance += amount
        ChangeMainBalance(-amount)
        if amount == 0:
            raise Exception("change zero amount")
        if amount > 0:
            print(f'add {amount} to {self.Name} : {self.Balance}')
        else:
            print(f'remove {-amount} from {self.Name} : {self.Balance}')

    @staticmethod
    def Transfer(amount: int, payer: 'ClientBank', reciver: 'ClientBank'):
        if amount <= 0:
            raise ValueError('Transferring a negative amount')
        print(f'Transfer {amount} from {payer.Name} to {reciver.Name}.')
        payer.change(-amount)
        reciver.change(amount)

    def __str__(self):
        return f'{self.Account}.{str(self.Name).capitalize()} : {self.Balance}'
