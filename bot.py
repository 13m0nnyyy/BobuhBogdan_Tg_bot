import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

#токен
API_TOKEN = "8569352099:AAG68TPFnYk97NHwQhp46PIJQmY1pDio6is"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

#обробник старту
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привіт, я твій бот, напиши /help щоб дізнатись про мене🎉")

#команда help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Ось що я вмію:\n/start - привітання👍\n/help - довідка✉️\n/about - про мене👌\n/joke - анекдот😂\n/bye - прощання🖐️")

#команда about
@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("Я був створений Бобухом Богданом📑")

#команда joke
@dp.message(Command("joke"))
async def joke_command(message: Message):
    await message.answer("Чому комп’ютер пішов у спортзал? Щоб прокачати свої байти!🤣😂")

#команда bye
@dp.message(Command("bye"))
async def bye_command(message: Message):
    await message.answer("Допобачення, гарного вам дня🖐️")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
