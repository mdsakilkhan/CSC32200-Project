from lxml import etree, objectify
import sys
import Users
from datetime import datetime

customer1 = Users.Customer(first_name="Joshua",
                           last_name="Chang",
                           date_of_birth=datetime(month=4, day=16, year=2021),
                           email='Joshua.chang998@gmail.com')

print(customer1.date_of_birth)

tree = etree.parse("Users.xml")
print(etree.tostring(tree, pretty_print=True))
