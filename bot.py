import logging
import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   await message.reply('Start')


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   await message.reply('Вы обратились к справке бота')


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)