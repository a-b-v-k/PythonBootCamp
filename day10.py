class BankAccount:
    def __init__(self):
        self.balance = 0
        self.interest = 2

    def deposit(self, amount):
        if(amount < 0):
            print("Invalid")
            return False
        else:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if(amount > self.balance or amount < 0):
            print("Insufficient balance")
            return False
        else:
            self.balance -= amount
        return self.balance

    def accumulate_interest(self):
        self.balance += self.balance * self.interest/100
        return self.balance

class ChildrensAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest = 0

    def accumulate_interest(self):
        self.balance += 10
        return self.balance

class OverdraftAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_penalty = 40

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= self.overdraft_penalty
            return False
        else:
            self.balance -= amount
            return self.balance

    def accumulate_interest(self):
        if self.balance < 0:
            return False
        else:
            self.balance += self.balance * self.interest/100
            return self.balance

def Run_bank_prog():
    basic_account = BankAccount()
    basic_account.deposit(600)
    print("Basic account has ${}".format(basic_account.balance))
    basic_account.withdraw(17)
    print("Basic account has ${}".format(basic_account.balance))
    basic_account.accumulate_interest()
    print("Basic account has ${}".format(basic_account.balance))
    print()

    childs_account = ChildrensAccount()
    childs_account.deposit(34)
    print("Child's account has ${}".format(childs_account.balance))
    childs_account.withdraw(17)
    print("Child's account has ${}".format(childs_account.balance))
    childs_account.accumulate_interest()
    print("Child's account has ${}".format(childs_account.balance))
    print()

    overdraft_account = OverdraftAccount()
    overdraft_account.deposit(12)
    print("Overdraft account has ${}".format(overdraft_account.balance))
    overdraft_account.withdraw(17)
    print("Overdraft account has ${}".format(overdraft_account.balance))
    overdraft_account.accumulate_interest()
    print("Overdraft account has ${}".format(overdraft_account.balance))


class Item(object):
    def __init__(self,itemname,itemprice):
        self.itemname = itemname
        self.itemprice = itemprice

    def ChangeItemPrice(self,newprice):
        self.itemprice = newprice

class Cart(dict):      #cart dict format:  {itemname:[price,number]}
    def ShowCart(self):
        return self   

class User(object):
    def __init__(self, name):    
        self.name = name
        self.cartlist = []
        self.cartlist.append(Cart())

    def AddCart(self):
        self.cartlist.append(Cart())

    def GetCart(self, cartindex = 0):
        if cartindex < len(self.cartlist):
            return self.cartlist[cartindex]
        return False

    def BuyItem(self, item, itemnum, cartindex = 0):
        if item.itemname in self.cartlist[cartindex].keys():
            self.cartlist[cartindex][item.itemname][1] += itemnum
        else:
            self.cartlist[cartindex].update({item.itemname:[item.itemprice, itemnum]})

def Run_Ecommerce_prog():
    item1 = Item('apple', 7.8)
    item2 = Item('pear', 5)   

    user1 = User('John')

    user1.BuyItem(item1, 5)
    print("user1 cart0 have: %s" % user1.GetCart(0).ShowCart())

    user1.BuyItem(item2, 6)
    print("user1 cart0 have: %s" % user1.GetCart(0).ShowCart())


    user1.AddCart()
    user1.BuyItem(item1, 5, 1)
    print("user1 cart1 have: %s" % user1.GetCart(1).ShowCart())

if __name__ == '__main__':
    print("Bank program:")
    Run_bank_prog()
    print("\nEcommnerce program:")
    Run_Ecommerce_prog()