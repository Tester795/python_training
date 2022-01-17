from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='firstname']"), contact.firstname)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='middlename']"), contact.middle_name)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='lastname']"), contact.lastname)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='nickname']"), contact.nickname)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='title']"), contact.title)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='company']"), contact.company)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address']"), contact.address)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='home']"), contact.home_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='mobile']"), contact.mobile_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='work']"), contact.work_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='fax']"), contact.fax_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email']"), contact.email)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email2']"), contact.email_2)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email3']"), contact.email_3)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='homepage']"), contact.home_page_url)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bday']").send_keys(contact.birthday)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bmonth']").send_keys(contact.birth_month)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='byear']"), contact.birth_year)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='new_group']").send_keys(contact.group)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address2']"), contact.address_2)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='phone2']"), contact.home_telephone_2)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='notes']"), contact.notes)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home page").click()

    def delete_first(self):
        wd = self.app.wd
        # select first contact on home page
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def delete_all(self):
        wd = self.app.wd
        # select all checkbox on home page
        wd.find_element(By.XPATH, "//*[@id='MassCB']").click()
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def delete(self, contact_lastname, contact_firstname):
        wd = self.app.wd
        # find contact with specific last name and first name
        wd.find_element(By.XPATH, "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='" + contact_lastname
                        + "'] and ./td[3][text()='" + contact_firstname + "'] ]/td[1]/input").click()
        # submit deletion
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def modify(self, old_contact, new_contact):
        wd = self.app.wd
        # find contact with specific last name and first name
        wd.find_element(By.XPATH, "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='" + old_contact.lastname
                        + "'] and ./td[3][text()='" + old_contact.firstname + "'] ]/td[8]/a").click()

        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='firstname']"), new_contact.firstname)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='middlename']"), new_contact.middle_name)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='lastname']"), new_contact.lastname)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='nickname']"), new_contact.nickname)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='title']"), new_contact.title)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='company']"), new_contact.company)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address']"), new_contact.address)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='home']"), new_contact.home_telephone)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='mobile']"), new_contact.mobile_telephone)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='work']"), new_contact.work_telephone)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='fax']"), new_contact.fax_telephone)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email']"), new_contact.email)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email2']"), new_contact.email_2)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email3']"), new_contact.email_3)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='homepage']"), new_contact.home_page_url)

        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bday']").send_keys(new_contact.birthday)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bmonth']").send_keys(new_contact.birth_month)

        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='byear']"), new_contact.birth_year)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address2']"), new_contact.address_2)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='phone2']"), new_contact.home_telephone_2)
        self.app.change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='notes']"), new_contact.notes)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='update']").click()

        wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))

    def exist(self, contact_lastname, contact_firstname):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH,
                                    "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='"
                                    + contact_lastname + "'] and ./td[3][text()='" + contact_firstname
                                    + "'] ]/td[1]/input")) > 0
