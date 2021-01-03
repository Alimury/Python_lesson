# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    app.group.test_edit(Group(name="new test1"))



def test_edit_group_header(app):
    app.group.test_edit(Group(header="new test1"))



