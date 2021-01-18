from model.add_new import Add_New
from random import randrange



def test_delete_some_new(app):
    if app.contact.count() == 0:
        app.contact.create_new(Add_New(firstname="Sidorov"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert old_contact == new_contact
