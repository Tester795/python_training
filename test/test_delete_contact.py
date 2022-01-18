# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(
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
                group="Group 1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_contact(app):
    test_contact = Contact(
            firstname="Contact for deletion",
            middle_name="test",
            lastname="Contact for deletion",
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

    if not app.contact.exist(test_contact.firstname, test_contact.lastname):
        app.contact.create(test_contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete(test_contact.lastname, test_contact.firstname)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.remove(test_contact)
    assert old_contacts == new_contacts

def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(
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
                group="Group 1"))
    app.contact.delete_all()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0

