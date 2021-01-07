# -*- coding: utf-8 -*-
from model.add_new import Add_New


def test_cont_edit(app):
    if app.contact.count() == 0:
        app.contact.create_new(Add_New(firstname="Sidorov"))
    old_contact = app.contact.get_contact_list()
    cont = Add_New(firstname="Smirnov")
    cont.id = old_contact[0].id
    app.contact.test_edit_add(cont)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = cont
    assert sorted(old_contact, key=Add_New.id_or_max) == sorted(old_contact, key=Add_New.id_or_max)

