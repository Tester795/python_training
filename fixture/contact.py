from datetime import time
from telnetlib import EC

from attr import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    contact_cache = None

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

        self.fill_contact_form(contact)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='new_group']").send_keys(contact.group)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_by_index(index)
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(
            lambda method: (wd.current_url.endswith("addressbook/") and len(wd.find_elements(By.ID, "maintable")) > 0))
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select all checkbox on home page
        wd.find_element(By.XPATH, "//*[@id='MassCB']").click()
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(
            lambda method: (wd.current_url.endswith("addressbook/") and len(wd.find_elements(By.ID, "maintable")) > 0))
        self.contact_cache = None

    def delete(self, contact_lastname, contact_firstname):
        wd = self.app.wd
        self.open_contacts_page()
        # find contact with specific last name and first name
        wd.find_element(By.XPATH,
                        "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='%s'] and ./td[3][text()='%s']]/td[1]/input"
                        % (contact_lastname, contact_firstname)).click()
        # submit deletion
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(lambda method: (wd.current_url.endswith("addressbook/") and len(wd.find_elements(By.ID, "maintable")) > 0))
        self.contact_cache = None

    def fill_contact_form(self, new_contact):
        wd = self.app.wd
        self.app.change_field_value("//*[@id='content']/form/input[@name='firstname']", new_contact.firstname)
        self.app.change_field_value("//*[@id='content']/form/input[@name='middlename']", new_contact.middle_name)
        self.app.change_field_value("//*[@id='content']/form/input[@name='lastname']", new_contact.lastname)
        self.app.change_field_value("//*[@id='content']/form/input[@name='nickname']", new_contact.nickname)
        self.app.change_field_value("//*[@id='content']/form/input[@name='title']", new_contact.title)
        self.app.change_field_value("//*[@id='content']/form/input[@name='company']", new_contact.company)
        self.app.change_field_value("//*[@id='content']/form/textarea[@name='address']", new_contact.address)
        self.app.change_field_value("//*[@id='content']/form/input[@name='home']", new_contact.home_telephone)
        self.app.change_field_value("//*[@id='content']/form/input[@name='mobile']", new_contact.mobile_telephone)
        self.app.change_field_value("//*[@id='content']/form/input[@name='work']", new_contact.work_telephone)
        self.app.change_field_value("//*[@id='content']/form/input[@name='fax']", new_contact.fax_telephone)
        self.app.change_field_value("//*[@id='content']/form/input[@name='email']", new_contact.email)
        self.app.change_field_value("//*[@id='content']/form/input[@name='email2']", new_contact.email_2)
        self.app.change_field_value("//*[@id='content']/form/input[@name='email3']", new_contact.email_3)
        self.app.change_field_value("//*[@id='content']/form/input[@name='homepage']", new_contact.home_page_url)

        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bday']").send_keys(new_contact.birthday)
        wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bmonth']").send_keys(new_contact.birth_month)

        self.app.change_field_value("//*[@id='content']/form/input[@name='byear']", new_contact.birth_year)
        self.app.change_field_value("//*[@id='content']/form/textarea[@name='address2']", new_contact.address_2)
        self.app.change_field_value("//*[@id='content']/form/input[@name='phone2']", new_contact.home_telephone_2)
        self.app.change_field_value("//*[@id='content']/form/textarea[@name='notes']", new_contact.notes)

    def modify(self, new_contact):
        wd = self.app.wd
        self.open_contacts_page()

        wd.find_element(By.XPATH, "//*[@id='%s']//..//..//td[8]/a" % str(new_contact.id)).click()

        self.fill_contact_form(new_contact)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements(By.NAME, "selected[]")[index].find_element(By.XPATH, "//..//..//td[8]/a").click()

        self.fill_contact_form(new_contact_data)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def exist(self, contact_lastname, contact_firstname):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.XPATH,
                                    "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='%s'] and ./td[3][text()='%s']]/td[1]/input"
                                    % (contact_lastname, contact_firstname))) > 0

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []

            WebDriverWait(wd, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@id='maintable']//tr[@name='entry']")))
            # WebDriverWait(wd, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))
            rows = wd.find_elements(By.XPATH, "//table[@id='maintable']//tr[@name='entry']")

            for row in rows:
                WebDriverWait(row, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "td")))

                cells = row.find_elements(By.TAG_NAME, "td")
                contact_id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=contact_id))
        return list(self.contact_cache)

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
