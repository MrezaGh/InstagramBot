from time import sleep
from selenium import webdriver


class SeleniumBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

        self.browser.get('https://www.instagram.com/')

    def login(self):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
