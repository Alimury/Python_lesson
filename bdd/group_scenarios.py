from pytest_bdd import scenario
from bdd.contact_steps import *
from bdd.group_steps import *


@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass

@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass

@scenario('groups.feature', 'Modification a group')
def test_edit_group():
    pass

@scenario("contact.feature", "Add new contact")
def test_add_new_contact():
    pass


@scenario("contact.feature", "Delete a contact")
def test_delete_contact():
    pass

@scenario("contact.feature", "Modification a contact")
def test_edit_contact():
    pass
