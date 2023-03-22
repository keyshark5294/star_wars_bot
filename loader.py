from config_data import config
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)