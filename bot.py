from instapy_bot import InstaPyBot
from secrets import instagram_username, instagram_pass


bot = InstaPyBot(instagram_username, instagram_pass)

bot.login()
bot.like_by_tag(["bmw", "taylor_swift"])
bot.block_tags(['nsfw', 'nude'])
bot.follow(percentage=50)
bot.comment(percentage=50)




