# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):

    if app.group.count() == 0:
        app.group.create(Group(name="First group", header="Group header", footer="group footer"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_group(app):
    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)
    old_groups = app.group.get_group_list()
    app.group.delete(test_group.name)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.remove(test_group)
    assert old_groups == new_groups
