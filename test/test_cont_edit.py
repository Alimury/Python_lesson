# -*- coding: utf-8 -*-
from model.add_new import Add_New
from random import randrange


def test_cont_edit(app, data_contact):
    if app.contact.count() == 0:
        app.contact.create_new(Add_New(firstname="Petr", lastname="Petrov"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    cont = data_contact
    cont.id = old_contact[index].id
    app.contact.modify_contact_by_index(cont, index)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = cont
    assert sorted(old_contact, key=Add_New.id_or_max) == sorted(new_contact, key=Add_New.id_or_max)


# def test_cont_edit(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Add_New(firstname="Petr", lastname="Petrov"))
#     old_contact = app.contact.get_contact_list()
#     index = randrange(len(old_contact))
#     cont = Add_New(firstname="Semen", lastname="Sidorov")
#     cont.id = old_contact[index].id
#     app.contact.modify_contact_by_index(cont, index)
#     assert len(old_contact) == app.contact.count()
#     new_contact = app.contact.get_contact_list()
#     old_contact[index] = cont
#     assert sorted(old_contact, key=Add_New.id_or_max) == sorted(new_contact, key=Add_New.id_or_max)