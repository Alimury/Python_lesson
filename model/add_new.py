


class Add_New:

    def __init__(self, firstname=None, lastname=None, address=None, telephone=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.telephone = telephone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

