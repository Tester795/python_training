import re
from random import randrange


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


def test_random_contact_info_same_on_home_and_edit_pages(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts)) 
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == formate_like_on_home_page(contact_from_edit_page.firstname)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.lastname == formate_like_on_home_page(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == formate_like_on_home_page(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[/.() -]", "", s, re.DOTALL)


def formate_like_on_home_page(s):
    if s != "" and s is not None:
        return (re.sub(' +', ' ', s)).rstrip(' ')


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_telephone
                                                               , contact.mobile_telephone
                                                               , contact.work_telephone
                                                               , contact.home_telephone_2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email
                                                                                , contact.email_2, contact.email_3])))

