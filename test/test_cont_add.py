# -*- coding: utf-8 -*-
from model.add_new import Add_New


def test_add_new(app):
    old_contact = app.contact.get_contact_list()
    cont = Add_New(firstname="Petr", lastname="Petrov")
    app.contact.create_new(cont)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(cont)
    assert sorted(old_contact, key=Add_New.id_or_max) == sorted(new_contact, key=Add_New.id_or_max)


