# -*- coding: utf-8 -*-
from model.add_new import Add_New


def test_cont_edit(app):
    if app.contact.count() == 0:
        app.contact.create_new(Add_New(firstname="Sidorov"))
    app.contact.test_edit_add(Add_New(firstname="Smirnov"))