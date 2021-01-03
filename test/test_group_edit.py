# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test4"))
    app.group.test_edit(Group(name="new test1"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test4"))
    app.group.test_edit(Group(header="new test1"))



