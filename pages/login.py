from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import requests


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(25)


class LoginPage(BasePage):
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    submit_button = (By.ID, 'login-button')
    failed_error_message = (By.NAME, 'error')

    # todo add exception handling to all methods

    def set_email(self, username):
        set_username = self.driver.find_element(*LoginPage.username_field)
        set_username.send_keys(username)

    def set_password(self, password):
        set_password = self.driver.find_element(*LoginPage.password_field)
        set_password.send_keys(password)

    def click_login_button(self):
        submit_button = self.driver.find_element(*LoginPage.submit_button)
        submit_button.click()

    def find_error_button(self):

        try:
            error_box = self.driver.find_element_by_xpath('//*[@id="login_button_container"]/div/form/div[3]')
            return error_box
        except NoSuchElementException:
            return False
        # todo still undecided how to handle fail case - whether to surface stack tracef


    def get_error_message(self):
        error_message = self.driver.find_element_by_xpath('//*[@id="login_button_container"]/div/form/div[3]/h3')
        return error_message.text

    def get_status(self, url):
        return requests.get(url).status_code

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def request_main_png_asset(self, url):
        return requests.get(url).status_code
