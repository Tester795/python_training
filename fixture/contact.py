from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
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

        def change_value(element, value):
            # element.send_keys(keys.Keys.CONTROL + "a")
            # element.send_keys(keys.Keys.DELETE)
            element.send_keys(value)

        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='firstname']"), new_contact.firstname)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='middlename']"), new_contact.middle_name)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='lastname']"), new_contact.lastname)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='nickname']"), new_contact.nickname)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='title']"), new_contact.title)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='company']"), new_contact.company)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address']"), new_contact.address)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='home']"), new_contact.home_telephone)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='mobile']"), new_contact.mobile_telephone)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='work']"), new_contact.work_telephone)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='fax']"), new_contact.fax_telephone)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email']"), new_contact.email)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email2']"), new_contact.email_2)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email3']"), new_contact.email_3)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='homepage']"), new_contact.home_page_url)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bday']"), new_contact.birthday)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bmonth']"), new_contact.birth_month)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='byear']"), new_contact.birth_year)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address2']"), new_contact.address_2)
        change_value(
            wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='phone2']"), new_contact.home_telephone_2)
        change_value(
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
