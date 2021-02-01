from model.add_new import Add_New
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    # symbols = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Add_New(firstname="", lastname="", address="",
                    email="", email2="", email3="", homephone="", mobilephone="", workphone="", secondaryphone="")] + [
    Add_New(firstname=random_string('firstname', 10), lastname=random_string('lastname', 20), address=random_string('address', 20),
            email=random_string('email', 20), email2=random_string('email2', 20), email3=random_string('email3', 20),
            homephone=random_string('homephone', 10), mobilephone=random_string('mobilephone', 10),
            workphone=random_string('workphone', 10), secondaryphone=random_string('secondaryphone', 10))
    for name in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))