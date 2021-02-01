# -*- coding: utf-8 -*-
from model.add_new import Add_New



def test_add_new(app, data_contact):
    add_new = data_contact
    old_contact = app.contact.get_contact_list()
    app.contact.create_new(add_new)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(add_new)
    assert sorted(old_contact, key=Add_New.id_or_max) == sorted(new_contact, key=Add_New.id_or_max)


