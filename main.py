from loader import dp, bot
import handlers 
from aiogram import executor


if __name__ == "__main__":
    executor.start_polling(dp)
