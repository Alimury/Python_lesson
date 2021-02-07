# -*- coding: utf-8 -*-
from model.add_new import Add_New
import random


def test_cont_edit(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Add_New(firstname="Petr", lastname="Petrov"))
    old_contact = db.get_contact_list()
    edit_contact = random.choice(old_contact)
    new_contact_data = Add_New(firstname="Petr1", lastname="Petrov1")
    app.contact.modify_contact_by_id(edit_contact.id, new_contact_data)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    edit_contact.firstname = new_contact_data.firstname
    edit_contact.lastname = new_contact_data.lastname
    assert old_contact == new_contact
    if check_ui:
        assert sorted(old_contact, key=Add_New.id_or_max) == sorted(app.contact.get_contact_list(), key=Add_New.id_or_max)

