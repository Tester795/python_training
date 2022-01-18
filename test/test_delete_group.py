# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):

    if app.group.count() == 0:
        app.group.create(Group(name="First group", header="Group header", footer="group footer"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_group(app):
    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)
    old_groups = app.group.get_group_list()
    app.group.delete(test_group.name)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_delete_empty_group(app):
    test_group = Group(name="", header="", footer="")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)
    old_groups = app.group.get_group_list()
    app.group.delete(test_group.name)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

