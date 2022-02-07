# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_delete_first_contact(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        first_contact = Contact(
            firstname="test 2",
            middlename="test",
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
        app.contact.create(first_contact)

    old_contacts = db.get_contact_list()
    app.contact.delete_first()
    # assert app.contact.count() == len(old_contacts) - 1
    new_contacts = db.get_contact_list()  # app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_delete_some_contact(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        test_contact = Contact(
            firstname="test 2",
            middlename="test",
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
        app.contact.create(test_contact)
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = db.get_contact_list()
    old_contacts[index:index + 1] = []
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_delete_all_contacts(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(
                firstname="test 2",
                middlename="test",
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
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == 0
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
