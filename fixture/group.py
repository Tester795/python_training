from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        # ini group creation
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        # submit deletion
        wd.find_element(By.NAME, "selected[]").click()
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
