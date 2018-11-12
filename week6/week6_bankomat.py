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
    def __init__(self, account_dict, balance= 0):
        self.accounts = account_dict
        self.balance = int(balance)

"""class Card(object):
    def __init__(self, card_number, card_password):
        self.card_nr = card_number
        self.card_pass = card_password
        """
class ATM(object):
    def __init__(self, bank, account=0):
        self.account = account
        self.bank = bank
    def menu(self):

        number= input("Podaj numer konta: \n ")
        password = input("Podaj hasło: \n ")
        for account_number in self.bank.account_list:
            if account_number == number:
                if password == self.bank.accounts[account_number]:
                    self.account = self.bank.accounts(account_number)
                    print("ok!")
            print(self.account)
        print(password)
        if not self.account:
            print("Podane konto nie istnieje!")
        else:
            print("MENU: \n 1. Wyświetl saldo: \n 2. Wpłata \n 3. Wypłata \n ")
            numer_operacji = input("Podaj co chesz zrobić: ")
            if numer_operacji == 1:
                print(self.account.balance)


class Bank(object):
    def __init__(self, account_list):
        self.account_list = account_list

bank = Bank({
    "123" : Account("123", "haslo1"),
    "234" : Account ("234", 'hasło2'),
    "345" : Account ("345", "haslo3")
    #account_list = [account1, account2,account3]
})
#bank = Bank([account1, account2, account3])
print(bank.account_list)
atm = ATM(bank)
atm.menu()

#zadanie wyswietlanie hasla, wplaty i wyplaty pieniedzy

# program do fakturowania w hurtowni -