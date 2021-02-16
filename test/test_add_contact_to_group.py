from model.add_new import Add_New
from model.group import Group
import random
import allure

def test_add_contact_to_group(app, db, orm):
    with allure.step("Given if the list is empty new contact"):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Add_New(firstname="c_firstname", lastname="c_lastname",
                                       address="c_address", homephone="c_homef", email="c_email"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
        groups = db.get_group_list()
    with allure.step("When I select a contact and group and add contact to group"):
        for group in groups:
            list_group = orm.get_contacts_not_in_group(Group(id=group.id))
            if len(list_group) > 0:
                contact = random.choice(list_group)
                app.contact.add_contact_to_group(contact.id, group.id)
                break
            elif len(list_group) == 0:
                if group != groups[-1]:
                    continue
                else:
                    app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
                    groups = sorted(db.get_group_list(), key=Group.id_or_max)
                    group = groups[-1]
                    contact = random.choice(db.get_contact_list())
                    app.contact.add_contact_to_group(contact.id, group.id)
        print(contact)
    with allure.step("Then contact %s is in a group %s" % (contact, group)):
        list_cont = orm.get_contacts_in_group(Group(id=group.id))
        print(list_cont)
        assert contact in list_cont