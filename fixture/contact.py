from datetime import time
from telnetlib import EC

from attr import exceptions
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements(By.ID, "maintable")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create(self, contact):
        wd = self.app.wd

        wd.find_element(By.LINK_TEXT, "add new").click()

        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='firstname']"),
                              contact.firstname)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='middlename']"),
                              contact.middle_name)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='lastname']"),
                              contact.lastname)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='nickname']"),
                              contact.nickname)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='title']"), contact.title)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='company']"),
                              contact.company)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address']"),
                              contact.address)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='home']"),
                              contact.home_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='mobile']"),
                              contact.mobile_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='work']"),
                              contact.work_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='fax']"),
                              contact.fax_telephone)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email']"), contact.email)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email2']"),
                              contact.email_2)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='email3']"),
                              contact.email_3)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='homepage']"),
                              contact.home_page_url)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bday']").send_keys(contact.birthday)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bmonth']").send_keys(contact.birth_month)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='byear']"),
                              contact.birth_year)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='new_group']").send_keys(contact.group)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='address2']"),
                              contact.address_2)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='phone2']"),
                              contact.home_telephone_2)
        self.app.change_value(wd.find_element(By.XPATH, "//*[@id='content']/form/textarea[@name='notes']"),
                              contact.notes)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact on home page
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(lambda method: self.page_has_loaded())
        WebDriverWait(wd, 10).until(lambda method: len(wd.find_elements(By.ID, "maintable")) > 0)

    def delete_all(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select all checkbox on home page
        wd.find_element(By.XPATH, "//*[@id='MassCB']").click()
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(lambda method: self.page_has_loaded())
        WebDriverWait(wd, 10).until(lambda method: len(wd.find_elements(By.ID, "maintable")) > 0)

    def delete(self, contact_lastname, contact_firstname):
        wd = self.app.wd
        self.open_contacts_page()
        # find contact with specific last name and first name
        wd.find_element(By.XPATH, "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='" + contact_lastname
                        + "'] and ./td[3][text()='" + contact_firstname + "'] ]/td[1]/input").click()
        # submit deletion
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(lambda method: self.page_has_loaded())
        WebDriverWait(wd, 10).until(lambda method: len(wd.find_elements(By.ID, "maintable")) > 0)

    def modify(self, new_contact):
        wd = self.app.wd
        self.open_contacts_page()

        wd.find_element(By.XPATH, "//*[@id='" + new_contact.id + "']//..//..//td[8]/a").click()

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
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def exist(self, contact_lastname, contact_firstname):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.XPATH,
                                    "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='"
                                    + contact_lastname + "'] and ./td[3][text()='" + contact_firstname
                                    + "'] ]/td[1]/input")) > 0

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts = []

        WebDriverWait(wd, 10).until(lambda method: self.page_has_loaded())
        WebDriverWait(wd, 10).until(lambda method: len(wd.find_elements(By.ID, "maintable")) > 0)
        WebDriverWait(wd, 10).until(lambda method: len(wd.find_elements(By.TAG_NAME, "td")) > 0)
        WebDriverWait(wd, 10).until(lambda method: len(wd.find_elements(By.TAG_NAME, "tr")) > 0)

        for row in wd.find_elements(By.NAME, "entry"):
            wait = WebDriverWait(row, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, "//td[1]"))
                       and EC.presence_of_element_located((By.XPATH, "//td[2]"))
                       and EC.presence_of_element_located((By.XPATH, "//td[3]")))

            contact_id = row.find_element(By.NAME, "//td[1]/*[@name='selected[]']").get_attribute("value")
            lastname = row.find_element(By.XPATH, "//td[2]").text
            firstname = row.find_element(By.XPATH, "//td[3]").text
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=contact_id))
        return contacts

    def find(self):
        wd = self.app.wd
        element = wd.find_elements_by_id("data")
        if element:
            return element
        else:
            return False

    def page_has_loaded(self):
        wd = self.app.wd
        page_state = wd.execute_script('return document.readyState;')
        return page_state == 'complete'

    def wait_for_visibility(self, selector, timeout_seconds=10):
        retries = timeout_seconds
        while retries:
            try:
                element = self.get_via_css(selector)
                if element.is_displayed():
                    return element
            except (exceptions.NoSuchElementException,
                    exceptions.StaleElementReferenceException):
                if retries <= 0:
                    raise
                else:
                    pass

            retries = retries - 1
            time.sleep(1)
        raise exceptions.ElementNotVisibleException(
            "Element %s not visible despite waiting for %s seconds" % (
                selector, timeout_seconds)
        )
