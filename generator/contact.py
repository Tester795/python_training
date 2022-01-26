import jsonpickle
import os
import string
import random
import getopt
import sys
from model.contact import Contact


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


def random_prefix(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
               Contact(
                    firstname="", lastname="", address="",
                    email="", email_2="", email_3="", home_telephone="",
                    mobile_telephone="", work_telephone="", home_telephone_2=""
                )] + [
    Contact(
        firstname=random_prefix("firstname", 10),
        lastname=random_prefix("lastname", 10),
        address=random_prefix("address", 30),
        email=random_prefix("email", 10),
        email_2=random_prefix("email_2", 10),
        email_3=random_prefix("email_3", 10),
        home_telephone=random_prefix("home_phone", 5),
        mobile_telephone=random_prefix("mobile_phone", 11),
        work_telephone=random_prefix("work_phone", 11),
        home_telephone_2=random_prefix("home_phone_2", 5)
    ) for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
