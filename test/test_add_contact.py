# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    # contact.birthday = random.choice(app.contact.get_birthday_available_values())
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
