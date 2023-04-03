from loader import dp, bot
import handlers # noqa
from aiogram import executor


if __name__ == "__main__":
    executor.start_polling(dp)
