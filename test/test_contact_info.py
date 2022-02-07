import re
from random import randrange

from model.contact import Contact


def test_phones_info_same_on_home_and_edit_pages(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_info_same_on_detail_and_edit_pages(app):
    contact_from_detail_page = app.contact.get_contact_info_from_detail_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_detail_page.home_telephone == contact_from_edit_page.home_telephone
    assert contact_from_detail_page.work_telephone == contact_from_edit_page.work_telephone
    assert contact_from_detail_page.mobile_telephone == contact_from_edit_page.mobile_telephone
    assert contact_from_detail_page.home_telephone_2 == contact_from_edit_page.home_telephone_2


def test_contacts_info_on_home_page_matches_with_db_data(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(
            firstname="Contact firstname",
            middlename="test",
            lastname="Contact lastname",
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

    db_contacts = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    for db_contact in db_contacts:
        db_contact.all_emails_from_home_page = merge_emails_like_on_home_page(db_contact)
        db_contact.all_phones_from_home_page = merge_phones_like_on_home_page(db_contact)

    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    assert db_contacts == contacts_from_home_page

    #  Такая проверка специфична только для этого теста, поэтому не стала выносить равнение этих полей в Contact.__eq__
    assert list(map(lambda c: (c.address, c.all_emails_from_home_page, c.all_phones_from_home_page)
                    , contacts_from_home_page)) ==\
           list(map(lambda c: (c.address, c.all_emails_from_home_page, c.all_phones_from_home_page), db_contacts))


def clear(s):
    return re.sub("[/.() -]", "", s, re.DOTALL)


def formate_like_on_home_page(s):
    if s != "" and s is not None:
        return (re.sub(' +', ' ', s)).rstrip(' ')
    elif s == "":
        return s


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_telephone
                                                               , contact.mobile_telephone
                                                               , contact.work_telephone
                                                               , contact.home_telephone_2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email_2, contact.email_3]))
