from model.group import Group
from timeit import timeit
from model.add_new import Add_New


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False


def test_contact1_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Add_New(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Add_New.id_or_max) == sorted(db_list, key=Add_New.id_or_max)



