from selenium import webdriver
from secrets import instagram_username, instagram_pass
from login_page import LoginPage

browser = webdriver.Firefox()
browser.implicitly_wait(5)

login_page = LoginPage(browser)
login_page.login(instagram_username, instagram_pass)

browser.close()


