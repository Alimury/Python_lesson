from model.add_new import Add_New
from model.group import Group
import random


def test_del_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Add_New(firstname="c_firstname", lastname="c_lastname",
                                   address="c_address", homephone="c_homef", email="c_email"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    contact = random.choice(db.get_contact_list())
    groups = db.get_group_list()
    group = random.choice(groups)
    list_group = orm.get_contacts_in_group(Group(id=group.id))
    if contact in list_group: #проверяем, что контакт состоит в группе
        app.contact.remove_contact_from_group(contact.id, group.id)
    else:
        app.contact.add_contact_to_group(contact.id, group.id) # если контакт не в группе, добавляем его
        app.contact.remove_contact_from_group(contact.id, group.id) # а потом удаляем из группы
    list = orm.get_contacts_not_in_group(Group(id=group.id))
    print(contact)
    print(list)
    assert contact not in orm.get_contacts_in_group(Group(id=group.id))