# I used kwargs in a similar manner as the solution to this post:
# https://stackoverflow.com/questions/9728243/is-self-dict-updatekwargs-good-or-poor-style

class DeliveryCompany():
    pass


class ComputerPartCompany():
    pass


class Person():
    def __init__(self, first_name=None, last_name=None, date_of_birth=None, contact_num=None, email_address=None, address=None):
        self.id = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.contact_num = contact_num
        self.email_address = email_address
        self.address = address
        
class StoreClerk(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Customer(Person):
    def __init__(self, card_number=None, bank=None, security_num=None, balance=None, purchases=None, cart=None, orders=None, **kwargs):
        super().__init__(**kwargs)
        self.card_number = card_number
        self.bank = bank
        self.security_num = security_num
        self.balance = balance
        self.purchases = purchases
        self.cart = cart
        self.orders = orders

class Order():
    def __init__(self, items=None, purchase_date=None, subtotal=None, total=None):
        self.items = items
        self.purchase_date = purchase_date
        self.subtotal = subtotal
        self.total = total

