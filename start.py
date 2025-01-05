from ClientFile import ClientBank
from MM2 import *
import re

connect('parif')


def is_numeric(text):
    pattern = r'^-?\d+$'
    return bool(re.match(pattern, text))


def isValidName(name: str) -> bool:
    if len(name) >= 3 and name.isalpha():
        return True
    return False


def create_user():
    name = input('Enter name of new user:')
    if name == '':
        return
    if not isValidName(name):
        print('Invalid name.')
        create_user()
        return
    user = ClientBank()
    user.Name = name.lower()
    user.Account = IdGenerator()
    user.Balance = 0
    user.save()
    print(f'create {user.Name} with id: {user.Account}')


def change_balance():
    dev = input('Change Balance, Enter id: ')
    if dev == '':
        return
    user = GetUser(dev)
    if user is None:
        print('Not Exist')
        change_balance()
        return
    print(user)
    while True:
        amount = input('Deposit or withdrawal amount:')
        if not is_numeric(amount):
            print('Invalid amount.')
            continue
        amount = int(amount)
        if amount == 0:
            return
        if user.Balance < -amount:
            print('Out of balacne.')
            return
        user.change(amount)
        user.save()
        return


def GetUser(id: str) -> [ClientBank]:
    user = ClientBank.objects.filter(Account=id).first()
    return user


def transfer():
    PayerId = input('Enter Payer ID:')
    payer = GetUser(PayerId)
    print(payer)
    if payer is None:
        print('Not Exist.')
        return
    payer: ClientBank
    ReciverId = input('Enter reciver ID:')
    reciver = GetUser(ReciverId)
    reciver: ClientBank
    print(reciver)
    if reciver is None:
        print('Not Exist.')
        return
    amount = int(input('Transfer amount:'))
    if amount == 0:
        return
    if amount < 0:
        print('خیلی شیطونی')
        return
    if payer.Balance < amount:
        print('Out of balacne.')
        return
    ClientBank.Transfer(amount=amount, reciver=reciver, payer=payer)
    payer.save()
    reciver.save()


OrdList = {
    1: 'Create a new User',
    2: 'Change balance of user',
    3: 'Transfer',
    4: 'Exit'}

continue_ = True

while continue_:
    print('Choose one of the options:')
    for i in OrdList:
        print(i, OrdList[i], sep='.')
    option = int(input('option:'))
    if option == 1:
        create_user()
    elif option == 2:
        change_balance()
    elif option == 3:
        transfer()
    elif option == 4:
        continue_ = False
    else:
        print('Wrong choice')
    print('---------------------')
