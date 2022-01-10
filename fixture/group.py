from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        # ini group creation
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(value)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        # submit deletion
        self.select_first_group()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def delete(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        # select group with specific name
        if group_name != "":
            xpath = "//*[@id='content']//span[@class='group' and text()='" + group_name + "']/input"
        else:
            xpath = "//*[@id='content']//span[@class='group' and not(text())]/input"

        wd.find_element(By.XPATH, xpath).click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def modify(self, group_name, new_group):
        wd = self.app.wd
        self.open_groups_page()
        # select group with specific name
        if group_name != "":
            xpath = "//*[@id='content']//span[@class='group' and text()='" + group_name + "']/input"
        else:
            xpath = "//*[@id='content']//span[@class='group' and not(text())]/input"

        wd.find_element(By.XPATH, xpath).click()
        # init modify
        wd.find_element(By.NAME, "edit").click()

        # fill group form with new values
        wd.find_element(By.NAME, "group_name").send_keys(keys.Keys.CONTROL + "a")
        wd.find_element(By.NAME, "group_name").send_keys(keys.Keys.DELETE)
        wd.find_element(By.NAME, "group_name").send_keys(new_group.name)
        wd.find_element(By.NAME, "group_header").send_keys(keys.Keys.CONTROL + "a")
        wd.find_element(By.NAME, "group_header").send_keys(keys.Keys.DELETE)
        wd.find_element(By.NAME, "group_header").send_keys(new_group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(keys.Keys.CONTROL + "a")
        wd.find_element(By.NAME, "group_footer").send_keys(keys.Keys.DELETE)
        wd.find_element(By.NAME, "group_footer").send_keys(new_group.footer)

        # submit modify
        wd.find_element(By.NAME, "update").click()

        self.return_to_groups_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def exist(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        if group_name != "":
            xpath = "//*[@id='content']//span[@class='group' and text()='" + group_name + "']/input"
        else:
            xpath = "//*[@id='content']//span[@class='group' and not(text())]/input"
        return len(wd.find_elements(By.XPATH, xpath)) > 0
