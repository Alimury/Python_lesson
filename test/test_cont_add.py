# -*- coding: utf-8 -*-
from model.add_new import Add_New
#import allure


def test_add_new(app, db, json_contact, check_ui):
    add_new = json_contact
#    with allure.step("Given checking for contact"):
    old_contact = db.get_contact_list()
#    with allure.step("When a contact is added %s to the list" % add_new):
    app.contact.create_new(add_new)
#    with allure.step("Then the new contact list is equal to the old list with the added contact"):
    new_contact = db.get_contact_list()
    old_contact.append(add_new)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(old_contact, key=Add_New.id_or_max) == sorted(app.contact.get_contact_list(), key=Add_New.id_or_max)


