# -*- coding: utf-8 -*-
import pytest
import random
import string

from model.group import Group


def random_prefix(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_prefix("name", 10), header=random_prefix("header", 20), footer=random_prefix("footer", 20))
    for i in range(5)
]

# test_data = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_prefix("name", 10)]
#     for header in ["", random_prefix("header", 20)]
#     for footer in ["", random_prefix("footer", 20)]
# ]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
