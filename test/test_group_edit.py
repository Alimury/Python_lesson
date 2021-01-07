# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test4"))
    old_groups = app.group.get_group_list()
    app.group.test_edit(Group(name="new test1", footer="new test"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test4"))
    old_groups = app.group.get_group_list()
    app.group.test_edit(Group(header="new test1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



