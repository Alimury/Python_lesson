# -*- coding: utf-8 -*-
from model.group import Group



def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test4"))
    old_groups = app.group.get_group_list()
    group = Group(name="new test1", footer="new test")
    group.id = old_groups[0].id
    app.group.test_edit(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test4"))
    old_groups = app.group.get_group_list()
    group = Group(name="new test1", header="new test1")
    group.id = old_groups[0].id
    app.group.test_edit(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



