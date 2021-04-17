# Major overhaul in constructor logic:
# I switched from using **kwargs to what it is now.
# Check out this stackoverflow post: https://stackoverflow.com/questions/9728243/is-self-dict-updatekwargs-good-or-poor-style
class DeliveryCompany():
    pass


class ComputerPartCompany():
    pass


class Person():
    def __init__(self, first_name=None, last_name=None, date_of_birth=None, contact_num=None, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.contact_num = contact_num
        self.email = email
        self.address = address


class StoreClerk():
    def __init__(self):
        super().__init__(self)


class Customer(Person):
    def __init__(self, card_number=None, bank=None, security_num=None, balance=None, purchase=None, cart=None, orders=None):
        super().__init__(self)
        # Payment information
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
