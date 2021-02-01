from model.add_new import Add_New
import random
import string


constant = [
    Add_New(firstname="firstname1", lastname='lastname1', address='address1',
            email='email1_1', email2='email2_1', email3='email3_1',
            homephone='homephone1', mobilephone='mobilephone1', workphone='workphone1', secondaryphone='secondaryphone1'),
    Add_New(firstname="firstname2", lastname='lastname2', address='address2',
            email='email2_1', email2='email2_2', email3='email3_2',
            homephone='homephone2', mobilephone='mobilephone2', workphone='workphone2',
            secondaryphone='secondaryphone2')
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    # symbols = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Add_New(firstname="", lastname="", address="", email="", homephone="")] + [
    Add_New(firstname=random_string('firstname', 10), lastname=random_string('lastname', 20), address=random_string('address', 20),
            email=random_string('email', 20), email2=random_string('email2', 20), email3=random_string('email3', 20),
            homephone=random_string('homephone', 10), mobilephone=random_string('mobilephone', 10), workphone=random_string('workphone', 10),
            secondaryphone=random_string('secondaryphone', 10))
    for name in range(2)
]