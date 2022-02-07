# -*- coding: utf-8 -*-
from model.contact import Contact
import random
from model.group import Group


def test_add_some_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Group", header="Group header", footer="group footer"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(
            firstname="Contact for add to group",
            middlename="test",
            lastname="Contact for add to group",
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
            notes="test", group=None))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group_by_id(contact.id, group.name)
    old_contacts_in_group.append(contact)
    new_contacts_in_group = orm.get_contacts_in_group(group)

    assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(old_contacts_in_group, key=Contact.id_or_max)
