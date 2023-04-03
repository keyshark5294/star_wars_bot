from loader import dp, bot
from aiogram import types 


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, я такой же любитель ЗВ как и ты. Ты можешь спросить у меня любую информацию про планеты, джадаев, дроидов и тд.")