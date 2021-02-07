# -*- coding: utf-8 -*-
from model.add_new import Add_New



def test_add_new(app, db, json_contact, check_ui):
    add_new = json_contact
    old_contact = db.get_contact_list()
    app.contact.create_new(add_new)
    new_contact = db.get_contact_list()
    old_contact.append(add_new)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(old_contact, key=Add_New.id_or_max) == sorted(app.contact.get_contact_list(), key=Add_New.id_or_max)


