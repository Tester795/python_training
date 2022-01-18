# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    contact = Contact(
            firstname="Contact for edit",
            middle_name="test",
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
            group="Group 1")
    if not app.contact.exist(contact.firstname, contact.lastname):
        app.contact.create(contact)

    old_contacts = app.contact.get_contact_list()
    contact.name = "Changed Firstname"
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



