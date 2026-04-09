import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

#токен
API_TOKEN = "8569352099:AAG68TPFnYk97NHwQhp46PIJQmY1pDio6is"
dp=Dispatcher()

#команда start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт, я твій бот, напиши /help щоб дізнатись про мене🎉(цей бот було створено Бобухом Богданом")

#команда help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("ось що я можу: /start - привітання👍, /about - про бота🤞"

#команда about
@dp.message(Сommand("about"))
async def about_command(message: Message):
    await message.answer("Я створений Бобухом Богданом👌")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main))


