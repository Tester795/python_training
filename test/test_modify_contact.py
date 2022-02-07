# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_some_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(
            firstname="Contact for edit",
            middlename="test",
            lastname="Contact for edit",
            nickname="test",
            title="test",
            company="test",
            address="test",
            home_telephone="54456",
            mobile_telephone="465",
            work_telephone="234",
            fax_telephone="224567",
            email="test",
            email_2="test",
            email_3="test",
            home_page_url="test",
            birthday="17",
            birth_month="December",
            birth_year="3456",
            address_2="test",
            home_telephone_2="test",
            notes="test",
            group="Group 1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_contacts.remove(contact)

    contact.name = "Changed Firstname"
    app.contact.modify_by_id(contact.id, contact)
    old_contacts.append(contact)

    new_contacts = db.get_contact_list()

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(),
                                                                     key=Contact.id_or_max)
