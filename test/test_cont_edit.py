# -*- coding: utf-8 -*-
from model.add_new import Add_New


def test_cont_edit(app):
    app.contact.test_edit_add(Add_New(firstname="Semen"))
