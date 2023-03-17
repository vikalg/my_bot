import logging
import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(text='Привет')
async def echo(message: types.Message):
    await message.answer('Приветствую тебя пользователь')

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   await message.reply('Start')

@dp.message_handler(commands="send")
async def send_animal(message: types.Message):
    animals_emojis = {"cat": "😺 ", "dog": "🐶", "unicorn": "🦄"}
    args = message.get_args()
    await message.answer(animals_emojis.get(args, f"Нет такого аргумента! Выбор : {', '.join(animals_emojis.keys())}"))  

@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   await message.reply('Вы обратились к справке бота')


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
