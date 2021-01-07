from model.add_new import Add_New


def test_delete_first_new(app):
    if app.contact.count() == 0:
        app.contact.create_new(Add_New(firstname="Sidorov"))
    old_contact = app.contact.get_contact_list()
    app.contact.test_delete_first_new()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    assert old_contact == new_contact
