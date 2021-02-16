from model.add_new import Add_New
import random
import allure


def test_delete_some_new(app, db, check_ui):
    with allure.step("Given if the list is empty new contact"):
        if len(db.get_contact_list()) == 0:
            app.contact.create_new(Add_New(firstname="Sidorov"))
    with allure.step("Given remembering a contact from bd"):
        old_contact = db.get_contact_list()
        contant = random.choice(old_contact)
    with allure.step("When a contact is removed %s from list" % contant):
        app.contact.delete_contact_by_id(contant.id)
    with allure.step("Then the new contact list is equal to the old list without the deleted contact"):
        new_contact = db.get_contact_list()
        assert len(old_contact) - 1 == len(new_contact)
        old_contact.remove(contant)
        assert old_contact == new_contact
        if check_ui:
            assert sorted(new_contact, key=Add_New.id_or_max) == sorted(app.contact.get_contact_list(), key=Add_New.id_or_max)