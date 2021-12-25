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
