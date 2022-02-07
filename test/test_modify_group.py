# -*- coding: utf-8 -*-
import random

from model.group import Group


def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="First group", header="Group header", footer="group footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    old_groups.remove(group)

    group.name = "Changed some group"
    app.group.modify_by_id(group.id, group)
    old_groups.append(group)

    new_groups = db.get_group_list()

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        print("CHECK_UI")
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
