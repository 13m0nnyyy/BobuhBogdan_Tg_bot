import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder


#токен
API_TOKEN = "8569352099:AAG68TPFnYk97NHwQhp46PIJQmY1pDio6is"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

#обробник старту з меню
@dp.message(Command("start"))
async def start(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Скажи Привіт🖐️", callback_data="say_hi")
    kb.button(text="Жарт😂", callback_data="joke")
    kb.button(text="Гід📑", callback_data="help")
    kb.button(text="Хто створив🤞", callback_data="about")
    kb.adjust(1)
    await message.answer("Натисни кнопку нижче👇", reply_markup=kb.as_markup())

#Кнопка привіт
@dp.callback_query(F.data == "say_hi")
async def say_hi(callback: CallbackQuery):
    await callback.message.answer("Привіт, друже! 🌟")
    await callback.answer()
#кнопка анекдот
@dp.callback_query(F.data == "joke")
async def joke(callback: CallbackQuery):
    await callback.message.answer("Чому Python не їде велосипедом? — Бо не має коліс! 😄")
    await callback.answer()
#кнопка хелп
@dp.callback_query(F.data == "help")
async def help(callback: CallbackQuery):
    await callback.message.answer("Ось що я вмію:\n/start - привітання👍\n/help - довідка✉️\n/about - про мене👌\n/joke - анекдот😂\n/bye - прощання🖐Ось що я вмію:\n/start - привітання👍\n/help - довідка✉️\n/about - про мене👌\n/joke - анекдот😂\n/bye - прощання🖐")
    await callback.answer()
#Кнопка хто створив
@dp.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    await callback.message.answer("️Я був створений Бобухом Богданом📑")
    await callback.answer()


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
    elif "дякую" in text:
        await message.answer("Будь ласка, був радий допомогти🫡")
    elif "історія" in text:
        await message.answer("8 жовтня 1408 року відбулась перша згадка Чернівців!👇")
    else:
        await message.answer("Вибач, не зрозумів повідомлення, я ще вчусь😯")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

