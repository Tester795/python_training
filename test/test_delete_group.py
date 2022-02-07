# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="First group", header="Group header", footer="group footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)

    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delete_group(app, db, check_ui):
    test_group = Group(name="First group", header="Group header", footer="group footer")
    old_groups = db.get_group_list()
    if not any(group.name == test_group.name for group in old_groups):
        app.group.create(test_group)
    old_groups = db.get_group_list()
    app.group.delete(test_group.name)
    new_groups = db.get_group_list()
    old_groups.remove(test_group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
