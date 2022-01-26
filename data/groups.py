import string
import random

from model.group import Group

testdata = [
    Group(name="random", header="random", footer="random"),
    Group(name="random", header="random", footer="random")
]


# def random_prefix(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_prefix("name", 10), header=random_prefix("header", 20), footer=random_prefix("footer", 20))
#     for i in range(5)
# ]


