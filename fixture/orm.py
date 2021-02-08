from pony.orm import *
from datetime import datetime
from model.group import Group
from model.add_new import Add_New
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(str, column="deprecated")

    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def converts_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.converts_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def converts_contacts_to_model(self, contacts):
        def convert(add_new):
            return Add_New(id=str(add_new.id), firstname=add_new.firstname, lastname=add_new.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.converts_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))