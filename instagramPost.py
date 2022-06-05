from instabot import Bot
# https://pypi.org/project/instabot/
import credentials

def post_photo(image_name, caption):

    bot = Bot()

    bot.login(username=credentials.username,
              password=credentials.password)

    bot.upload_photo(image_name, caption=caption)

