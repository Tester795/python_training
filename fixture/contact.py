import re

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
        if contact.group is not None:
            wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='new_group']").send_keys(contact.group)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % str(contact_id)).click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_by_index(index)
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(
            lambda method:
            (len(wd.find_elements(By.CLASS_NAME, "msgbox")) > 0)
        )
        assert wd.find_element(By.CLASS_NAME, "msgbox").text == "Record successful deleted"
        self.contact_cache = None

    def delete_by_id(self, contact_id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_by_id(contact_id)
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(
            lambda method:
            (len(wd.find_elements(By.CLASS_NAME, "msgbox")) > 0)
        )
        assert wd.find_element(By.CLASS_NAME, "msgbox").text == "Record successful deleted"
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select all checkbox on home page
        wd.find_element(By.XPATH, "//*[@id='MassCB']").click()
        wd.find_element(By.XPATH, "//*[@id='content']//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(
            lambda method:
            (len(wd.find_elements(By.CLASS_NAME, "msgbox")) > 0)
        )
        assert wd.find_element(By.CLASS_NAME, "msgbox").text == "Record successful deleted"
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
        WebDriverWait(wd, 10).until(
            lambda method:
            (len(wd.find_elements(By.CLASS_NAME, "msgbox")) > 0)
        )
        assert wd.find_element(By.CLASS_NAME, "msgbox").text == "Record successful deleted"
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

        if new_contact.birthday is not None:
            wd.find_element(By.XPATH, "//*[@id='content']/form/select[@name='bday']").send_keys(new_contact.birthday)
        if new_contact.birth_month is not None:
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

        # wd.find_elements(By.NAME, "entry")[index].find_element(By.XPATH, "//td[8]/a").click()
        wd.find_element(By.XPATH, "//*[@id='maintable']//tr[@name='entry'][%s]//td[8]/a" % str(index + 1)).click()
        self.fill_contact_form(new_contact_data)

        wd.find_element(By.XPATH, "//*[@id='content']/form/input[@name='update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_by_id(self, contact_id, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element(By.XPATH, "//a[@href='edit.php?id=%s']" % str(contact_id)).click()
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
        return \
            len(
                wd.find_elements(
                    By.XPATH,
                    "//*[@id='maintable']//tr[@name='entry' and ./td[2][text()='%s'] and ./td[3][text()='%s']]/td[1]/input"
                    % (contact_lastname, contact_firstname))
            ) > 0

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            rows = wd.find_elements(By.XPATH, "//table[@id='maintable']//tr[@name='entry']")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                contact_id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text  # .splitlines()
                all_phones = cells[5].text  # .splitlines()
                self.contact_cache.append(
                    Contact(
                        contact_id=contact_id
                        , firstname=firstname
                        , lastname=lastname
                        , address=address
                        # , home_telephone_2=all_phones[3]
                        # , work_telephone=all_phones[2]
                        # , mobile_telephone=all_phones[1]
                        # , home_telephone=all_phones[0]
                        , all_phones_from_home_page=all_phones
                        , all_emails_from_home_page=all_emails
                    )
                )
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_detail_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element(By.NAME, "firstname").get_attribute("value")
        last_name = wd.find_element(By.NAME, "lastname").get_attribute("value")
        contact_id = wd.find_element(By.NAME, "id").get_attribute("value")
        home_telephone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile_telephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        work_telephone = wd.find_element(By.NAME, "work").get_attribute("value")
        home_telephone_2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email_2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email_3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(
            contact_id=contact_id
            , firstname=first_name
            , lastname=last_name
            , home_telephone=home_telephone
            , mobile_telephone=mobile_telephone
            , work_telephone=work_telephone
            , home_telephone_2=home_telephone_2
            , address=address
            , email=email
            , email_2=email_2
            , email_3=email_3
        )

    def get_contact_info_from_detail_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_detail_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        home_telephone_2 = re.search("P: (.*)", text).group(1)
        return Contact(
            home_telephone=home_telephone
            , mobile_telephone=mobile_telephone
            , work_telephone=work_telephone
            , home_telephone_2=home_telephone_2
        )

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/edit.php")
                and len(wd.find_elements(By.XPATH, "//form[@name='theform']")) > 0):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def get_birthday_available_values(self):
        wd = self.app.wd
        self.open_add_new_page()
        options = wd.find_elements(By.XPATH, "//select[@name='bday']//option")
        available_values = []
        [available_values.append(option.text) for option in options]
        return available_values

    def get_birthmoth_available_values(self):
        wd = self.app.wd
        self.open_add_new_page()
        options = wd.find_elements(By.XPATH, "//select[@name='bmonth']//option")
        available_values = []
        list(map(lambda option: available_values.append(option.text), options))
        return available_values

    def get_group_available_values(self):
        wd = self.app.wd
        self.open_add_new_page()
        options = wd.find_elements(By.XPATH, "//select[@name='new_group']//option")
        available_values = []
        list(map(lambda option: available_values.append(option.text), options))
        return available_values
