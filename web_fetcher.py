from time import sleep
from selenium import webdriver
from secrets import instagram_username, instagram_pass

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')


username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(instagram_username)
password_input.send_keys(instagram_pass)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(5)

browser.close()