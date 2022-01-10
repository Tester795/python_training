# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    old_contact = Contact(
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

    new_contact = Contact(
            firstname="Changed",
            middle_name="Changed",
            lastname="Changed",
            nickname="Changed",
            title="Changed",
            company="Changed",
            address="Changed",
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
    if not app.contact.exist(old_contact.firstname, old_contact.lastname):
        app.contact.create(old_contact)
    app.contact.modify(old_contact, new_contact)



