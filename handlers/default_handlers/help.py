from loader import dp, bot 
from aiogram import types 


@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await bot.send_message(message.from_user.id, "Если вам не помог перезапуск бота и вы уверены что правильно составили запрос, то опишите свою проблему сообщением на @KeySharks")
    await bot.send_message(message.from_user.id, "Также можете присылать свои идеи на этот же аккаунт")