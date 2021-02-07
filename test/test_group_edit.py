# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test4"))
    old_groups = db.get_group_list()
    edit_group = random.choice(old_groups)
    new_group_data = Group(name="test5")
    app.group.modify_group_by_id(edit_group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    edit_group.name = new_group_data.name
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
