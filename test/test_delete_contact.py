# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    # from test.test_add_contact import test_add_contact
    # test_add_contact(app)
    app.contact.delete_first()


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
    app.contact.create(test_contact)
    app.contact.delete(test_contact.lastname, test_contact.firstname)


def test_delete_all_contacts(app):
    app.contact.delete_all()

