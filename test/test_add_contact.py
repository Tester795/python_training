# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        firstname="test 2",
        middle_name="test",
        lastname="test",
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
        group="Group 1")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
