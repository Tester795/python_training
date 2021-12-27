# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")

    test_group = Group(name="First group", header="Group header", footer="group footer")
    app.group.create(test_group)

    app.group.modify(test_group.name,
                     Group(name="Changed First group", header="Changed Group header", footer="Changed group footer"))
    app.session.logout()


def test_modify_nonempty_group_to_empty(app):
    app.session.login(username="admin", password="secret")

    test_group = Group(name="First group", header="Group header", footer="group footer")
    app.group.create(test_group)

    app.group.modify(test_group.name, Group(name="", header="", footer=""))
    app.session.logout()


def test_modify_empty_group_to_nonempty(app):
    app.session.login(username="admin", password="secret")

    test_group = Group(name="", header="", footer="")
    app.group.create(test_group)

    app.group.modify(test_group.name, Group(name="First group", header="Group header", footer="group footer"))
    app.session.logout()
