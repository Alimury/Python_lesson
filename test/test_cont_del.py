from model.add_new import Add_New
import random


def test_delete_some_new(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Add_New(firstname="Sidorov"))
    old_contact = db.get_contact_list()
    contant = random.choice(old_contact)
    app.contact.delete_contact_by_id(contant.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(contant)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Add_New.id_or_max) == sorted(app.contact.get_contact_list(), key=Add_New.id_or_max)