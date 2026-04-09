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
    await message.answer("Привіт, я історичний бот, напиши /help щоб дізнатись про мене🎉")

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

#обробка звичайного тексту
@dp.message()
async def echo_text(message: Message):
    text = message.text.lower()
    if "привіт" in text:
        await message.answer("вітаю вас!🖐️")
    elif "як справи" in text:
        await message.answer("У мене все добре, а у вас?😊")
    elif "що ти вмієш" in text:
        await message.answer("Я історичний бот, який виконує команди😉")
    elif "анекдот" in text:
        await message.answer("Чому комп’ютер пішов у спортзал? Щоб прокачати свої байти!🤣😂")
    elif "мені сумно" in text:
        await message.answer("Не сумуй, все буде добре!😋")
    elif "історія" in text:
        await message.answer("8 жовтня 1408 року відбулась перша згадка Чернівців!👇")
    else:
        await message.answer("Вибач, не зрозумів повідомлення, я ще вчусь😯")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
