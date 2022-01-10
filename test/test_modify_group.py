# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):

    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)

    app.group.modify_first_group(Group(name="Changed First group"))


def test_modify_group_header(app):
    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)

    app.group.modify_first_group(Group(header="Changed group header"))


def test_modify_group(app):

    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)

    app.group.modify(test_group.name,
                     Group(name="Changed First group", header="Changed Group header", footer="Changed group footer"))


def test_modify_nonempty_group_to_empty(app):

    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)

    app.group.modify(test_group.name, Group(name="", header="", footer=""))


def test_modify_empty_group_to_nonempty(app):

    test_group = Group(name="", header="", footer="")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)

    app.group.modify(test_group.name, Group(name="First group", header="Group header", footer="group footer"))
