# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    test_group = Group(name="First group", header="Group header", footer="group footer")
    if not app.group.exist(test_group.name):
        app.group.create(test_group)

    old_groups = app.group.get_group_list()
    test_group.name = "Changed First group"
    test_group.id = old_groups[0].id
    app.group.modify_first_group(test_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = test_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     test_group = Group(name="First group", header="Group header", footer="group footer")
#     if not app.group.exist(test_group.name):
#         app.group.create(test_group)
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="Changed group header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#

# deprecated
# def test_modify_group(app):
#
#     test_group = Group(name="First group", header="Group header", footer="group footer")
#     if not app.group.exist(test_group.name):
#         app.group.create(test_group)
#     old_groups = app.group.get_group_list()
#     app.group.modify(test_group.name,
#                      Group(name="Changed First group", header="Changed Group header", footer="Changed group footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
