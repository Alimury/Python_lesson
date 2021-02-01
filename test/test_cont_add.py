# -*- coding: utf-8 -*-
from model.add_new import Add_New
import pytest
from data.contact import constant as testdata



@pytest.mark.parametrize("add_new", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, add_new):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new(add_new)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(add_new)
    assert sorted(old_contact, key=Add_New.id_or_max) == sorted(new_contact, key=Add_New.id_or_max)


