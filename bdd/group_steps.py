
from pytest_bdd import given, when, then
from model.group import Group
import random

#_______________Создание группы
@given("a group list", target_fixture="group_list")
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header> and <footer>', target_fixture="new_group")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when("I add the group the list")
def add_new_group(app, new_group):
    app.group.create(new_group)


@then("the new group list is equal to the old list with ten added group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#__________________________Удаление группы
@given("a non-empty group list", target_fixture="non_empty_group_list")
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="del group"))
    return db.get_group_list()


@given("a random group from the list", target_fixture="random_group")
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when("I delete the group from the list")
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then("the new group list is equal to the old list without the deleted group")
def verify_group_delete(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#__________________________________Модификация группы
@given("a new name for edited group", target_fixture="new_group_data" )
def new_group_data(random_group):
    group = Group(name="test5")
    group.id = random_group.id
    return group

@when("I edit the group from the list")
def edit_group(app, new_group_data):
    app.group.modify_group_by_id(new_group_data.id, new_group_data)

@then("the new group list is equal to the old list without the edit group")
def checking_contact_change(db, check_ui, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(random_group)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)