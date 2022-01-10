# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="First group", header="Group header", footer="group footer"))
    app.group.delete_first()


def test_delete_group(app):
    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)
    app.group.delete(test_group.name)


def test_delete_empty_group(app):
    test_group = Group(name="", header="", footer="")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)
    app.group.delete(test_group.name)

