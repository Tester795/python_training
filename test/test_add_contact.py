# -*- coding: utf-8 -*-
import random
import string

import pytest

from model.contact import Contact


def random_prefix(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
                Contact(
                    firstname="", lastname="", address="",
                    email="", email_2="", email_3="", home_telephone="",
                    mobile_telephone="", work_telephone="", home_telephone_2=""
                )] \
            + [
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
                    home_telephone_2=random_prefix("home_phone_2", 5))
                for i in range(5)
            ]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    # contact.birthday = [random.choice(app.contact.get_birthday_available_values()) for i in range(random.randrange(2))]
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
