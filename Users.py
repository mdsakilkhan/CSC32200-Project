

class DeliveryCompany():
    pass


class ComputerPartCompany():
    pass


class Person():
    def __init__(self, **kwargs):
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.date_of_birth = kwargs['date_of_birth']
        self.contact_num = kwargs['contact_num']
        self.email = kwargs['email']
        self.address = kwargs['address']


class StoreClerk():
    def __init__(self, **kwargs):
        super.__init__(self, **kwargs)


class Customer(Person):
    def __init__(self, **kwargs):
        Person.__init__(self, **kwargs)

        self.balance = kwargs['balance']
        self.card_number = kwargs['card_number']
        self.purchases = kwargs['purchases']
