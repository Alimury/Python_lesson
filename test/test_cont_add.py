# -*- coding: utf-8 -*-
from model.add_new import Add_New
from sys import maxsize

def test_add_new(app):
    old_contact = app.contact.get_contact_list()
    cont = Add_New(firstname="Petrov", lastname="Petr")
    app.contact.create_new(cont)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(cont)
    def id_or_max(ct):
        if ct.id:
            return int(ct.id)
        else:
            return maxsize
    assert sorted(old_contact, key=id_or_max) == sorted(new_contact, key=id_or_max)


