#   ****BANKOMAT****
#class Card
#   - numer
#   - password
#class ATM  -> bankomat
#   - menu
#       - pobiera haslo/numer
#       - wyswietla stan konta
#       - obsluguje wplaty/wyplaty
#class Account
#   - numer
#   - stan konta
#class Bank
#   - lista kont


class Account(object):
    def __init__(self, account_number, account_password):
        self.account_nr = account_number
        self.account_pass =  account_password
        self.balance = 0

class Card(object):
    def __init__(self, card_number, card_password):
        self.card_nr = card_number
        self.card_pass = card_password
class ATM(object):
    def nr_account(self):
        input_nr_account= input("Podaj numer konta: \n ")
    def pass_account(self):
        input_pass_account = input("Podaj hasło: \n ")
class Bank(object):
    def __init__(self, account_list):
        self.account_list = account_list

account1 = ("1234", "haslo1")
account2 = ("234", 'hasło2')
account3 = ("345", "haslo3")
#account_list = [account1, account2,account3]
bank = Bank([account1, account2, account3])
print(bank.account_list)