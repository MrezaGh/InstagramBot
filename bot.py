from secrets import instagram_username, instagram_pass
from selenium_bot import SeleniumBot

bot = SeleniumBot(instagram_username, instagram_pass)

bot.login()

