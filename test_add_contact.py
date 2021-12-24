# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_contacts_page(wd)
        self.create_contact(wd,
                            Contact(firstname="test 2", middle_name="test", lastname="test", nickname="test", title="test",
                                    company="test", address="test", home_telephone="54456", mobile_telephone="465", work_telephone="234",
                                    fax_telephone="224567",
                                    email="test", email_2="test", email_3="test", home_page_url="test", birthday="17",
                                    birth_month="December",
                                    birth_year="3456", address_2="test", home_telephone_2="test", notes="test", group="Group 1"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create_contact(self, wd, contact):
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='firstname']").send_keys(contact.firstname)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='middlename']").send_keys(contact.middle_name)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='lastname']").send_keys(contact.lastname)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='nickname']").send_keys(contact.nickname)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='title']").send_keys(contact.title)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='company']").send_keys(contact.company)
        wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address']").send_keys(contact.address)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='home']").send_keys(contact.home_telephone)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='mobile']").send_keys(contact.mobile_telephone)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='work']").send_keys(contact.work_telephone)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='fax']").send_keys(contact.fax_telephone)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email']").send_keys(contact.email)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email2']").send_keys(contact.email_2)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email3']").send_keys(contact.email_3)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='homepage']").send_keys(contact.home_page_url)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bday']").send_keys(contact.birthday)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bmonth']").send_keys(contact.birth_month)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='byear']").send_keys(contact.birth_year)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='new_group']").send_keys(contact.group)
        wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address2']").send_keys(contact.address_2)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='phone2']").send_keys(contact.home_telephone_2)
        wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='notes']").send_keys(contact.notes)
        wd.find_element(By.XPATH, "//*[@id='content']/form/input[21]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_contacts_page(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
