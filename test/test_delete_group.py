# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()


def test_delete_group(app):
    app.session.login(username="admin", password="secret")

    # Следует ли для корректного выполнения этого теста инициировать необходимые данные для удаления? Например, выполнив пред-тест:
    # test_add_group(app)
    # Или просто добавить методы добавления группы из этого теста
    test_group = Group(name="First group", header="Group header", footer="group footer")
    app.group.create(test_group)

    # или ничего автоматически не готовить перед началом этого теста, но быть уверенным, что такая группа существует и есть что удалять

    app.group.delete(test_group.name)
    app.session.logout()


def test_delete_empty_group(app):
    app.session.login(username="admin", password="secret")
    test_group = Group(name="", header="", footer="")
    app.group.create(test_group)
    app.group.delete(test_group.name)
    app.session.logout()
