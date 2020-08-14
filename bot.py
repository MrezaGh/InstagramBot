from instapy_bot import InstaPyBot
from secrets import instagram_username, instagram_pass


bot = InstaPyBot(instagram_username, instagram_pass)

bot.login()


