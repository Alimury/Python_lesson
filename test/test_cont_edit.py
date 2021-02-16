# -*- coding: utf-8 -*-
from model.add_new import Add_New
import random
import allure


def test_cont_edit(app, db, check_ui):
    with allure.step("Given if the list is empty new contact"):
        if len(db.get_contact_list()) == 0:
            app.contact.create_new(Add_New(firstname="Petr", lastname="Petrov"))
    with allure.step("Given remembering a contact from bd"):
        old_contact = db.get_contact_list()
        edit_contact = random.choice(old_contact)
    with allure.step("Given a new data for edited contact"):
        new_contact_data = Add_New(firstname="Petr1", lastname="Petrov1")
    with allure.step("When editing a contact %s from list %s" % edit_contact.id, new_contact_data):
        app.contact.modify_contact_by_id(edit_contact.id, new_contact_data)
    with allure.step("Then the new contact list is equal to the old with the edit contact"):
        new_contact = db.get_contact_list()
        assert len(old_contact) == len(new_contact)
        edit_contact.firstname = new_contact_data.firstname
        edit_contact.lastname = new_contact_data.lastname
        assert old_contact == new_contact
        if check_ui:
            assert sorted(old_contact, key=Add_New.id_or_max) == sorted(app.contact.get_contact_list(), key=Add_New.id_or_max)

