from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    group_cache = None

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
        self.group_cache = None

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

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % group_id).click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        # select group with specific name
        if group_name != "":
            xpath = "//*[@id='content']//span[@class='group' and text()='%s']/input" % group_name
        else:
            xpath = "//*[@id='content']//span[@class='group' and not(text())]/input"

        wd.find_element(By.XPATH, xpath).click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        # submit deletion
        self.select_by_index(index)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_by_id(self, group_id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_id(group_id)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify(self, group_name, new_group):
        wd = self.app.wd
        self.open_groups_page()
        # select group with specific name
        if group_name != "":
            xpath = "//*[@id='content']//span[@class='group' and text()='%s']/input" % group_name
        else:
            xpath = "//*[@id='content']//span[@class='group' and not(text())]/input"

        wd.find_element(By.XPATH, xpath).click()
        # init modify
        wd.find_element(By.NAME, "edit").click()

        # fill group form with new values
        self.fill_group_form(new_group)

        # submit modify
        wd.find_element(By.NAME, "update").click()

        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.modify_by_index(0, new_group_data)

    def modify_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_index(index)
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_by_id(self, group_id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_id(group_id)
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def exist(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        if group_name != "":
            xpath = "//*[@id='content']//span[@class='group' and text()='%s']/input" % group_name
        else:
            xpath = "//*[@id='content']//span[@class='group' and not(text())]/input"
        return len(wd.find_elements(By.XPATH, xpath)) > 0

    def get_group_list(self):

        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                group_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))

        return list(self.group_cache)


