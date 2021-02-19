# -*- coding: utf-8 -*-
from model.group import Group
import random
#import allure

def test_edit_group_name(app, db, check_ui):
#    with allure.step("Given if the list is empty new group"):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test4"))
#    with allure.step("Given remembering a group from bd"):
    old_groups = db.get_group_list()
    edit_group = random.choice(old_groups)
#    with allure.step("Given a new data for edited group"):
    new_group_data = Group(name="test5")
#    with allure.step("When editing a group %s from list %s" % edit_group.id, new_group_data):
    app.group.modify_group_by_id(edit_group.id, new_group_data)
#    with allure.step("Then the new group list is equal to the old with the edit group"):
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    edit_group.name = new_group_data.name
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
