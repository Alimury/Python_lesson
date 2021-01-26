# -*- coding: utf-8 -*-
from model.add_new import Add_New
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Add_New(firstname="", lastname="", address="", email="", homephone="")] + [
    Add_New(firstname=random_string('firstname', 10), lastname=random_string('lastname', 20), address=random_string('address', 20),
            email=random_string('email', 20), email2=random_string('email2', 20), email3=random_string('email3', 20),
            homephone=random_string('homephone', 10), mobilephone=random_string('mobilephone', 10), workphone=random_string('workphone', 10),
            secondaryphone=random_string('secondaryphone', 10))
    for name in range(2)
]


@pytest.mark.parametrize("add_new", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, add_new):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new(add_new)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(add_new)
    assert sorted(old_contact, key=Add_New.id_or_max) == sorted(new_contact, key=Add_New.id_or_max)


