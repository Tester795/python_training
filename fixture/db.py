import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(
            host="127.0.0.1"
            , database="addressbook"
            , user="root"
            , password=""
            , autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, group_name, group_header, group_footer) = row
                group_list.append(Group(id=str(group_id), name=group_name, header=group_header, footer=group_footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, middlename, lastname from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (contact_id, firstname, middlename, lastname) = row
                contact_list.append(
                    Contact(contact_id=str(contact_id), firstname=firstname, middlename=middlename, lastname=lastname))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
