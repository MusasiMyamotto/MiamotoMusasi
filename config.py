from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMINS = [5496595509,]