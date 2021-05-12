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
    def __init__(self, password=None, card_number=None, bank=None, security_num=None, balance="0", purchases=None, cart=None, orders=None, **kwargs):
        super().__init__(**kwargs)
        self.password = password
        self.card_number = card_number
        self.bank = bank
        self.security_num = security_num
        self.balance = balance
        self.purchases = purchases
        self.cart = cart
        self.orders = orders

class Manager(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Order():
    def __init__(self, items=None, id=None, purchase_date=None, subtotal=None, total=None, **kwargs):
        self.items = items
        self.id = id
        self.purchase_date = purchase_date
        self.total = total

class ItemComment():
    def __init__(self, customer_name=None, item=None, description=None, **kwargs):
        self.customer_name = customer_name
        self.item = item
        self.description = description

class ClerkComment():
    def __init__(self, customer_name=None, clerk=None, description=None, **kwargs):
        self.customer_name = customer_name
        self.clerk = clerk
        self.description = description

class CompanyComment():
    def __init__(self, customer_name=None, company=None, description=None, **kwargs):
        self.customer_name = customer_name
        self.company = company
        self.description = description

class ItemWithDate():
    def __init__(self):
        self.id = None
        self.date = None