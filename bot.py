import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder, ReplyKeyboardMarkup

#токен
API_TOKEN = "8569352099:AAG68TPFnYk97NHwQhp46PIJQmY1pDio6is"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="/start", description="Головне меню 🏠"),
        BotCommand(command="/help", description="Гід по боту 📑"),
        BotCommand(command="/quiz", description="Вікторина про місто 👨‍🎓"),
        BotCommand(command="/about", description="Автор проекту 🤞"),
        BotCommand(command="/joke", description="Розсміши мене 😂"),
        BotCommand(command="/fact", description="Цікавий факт ✨"),
        BotCommand(command="/bye", description="Прощання 🖐")
    ]
    await bot.set_my_commands(main_menu_commands)

def get_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="Привіт 👋"), KeyboardButton(text="Жарт 😂"))
    builder.row(KeyboardButton(text="Гід 📑"), KeyboardButton(text="Вікторина 👨‍🎓")) # Ось вона!
    builder.row(KeyboardButton(text="Цікавий факт ✨"), KeyboardButton(text="Графік роботи 📈"))
    return builder.as_markup(resize_keyboard=True)

#обробник старту з меню
@dp.message(Command("start"))
async def start(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Скажи привіт🖐️", callback_data="say_hi")
    kb.button(text="Жарт😂", callback_data="joke")
    kb.button(text="Гід📑", callback_data="help1")
    kb.button(text="Хто створив🤞", callback_data="about")
    kb.button(text="Цікавий факт✨", callback_data="fact")
    kb.button(text="Графік роботи📈", callback_data="graphik")
    kb.button(text="Налаштування🔧", callback_data="settings")
    kb.adjust(1)

    main_reply_kb = get_reply_keyboard()

    await message.answer(
        "Вітаю! Я історичний бот на тематику Чернівців! \nНатисни кнопку нижче👇",
        reply_markup=main_reply_kb
    )

    await message.answer("Швидке меню за категоріями:", reply_markup=kb.as_markup())

#------------Кнопка привіт
@dp.callback_query(F.data == "say_hi")
async def say_hi(callback: CallbackQuery):
    await callback.message.answer(f"Привіт, {callback.from_user.full_name}! 🌟")
    await callback.answer()
#кнопка анекдот
@dp.callback_query(F.data == "joke")
async def joke(callback: CallbackQuery):
    await callback.message.answer("- Мамо, я хочу в Париж!\n- У нас є Париж вдома. \nПариж вдома: Чернівці, дощ, бруківка і пари в ЧНУ.")
    await callback.answer()
#кнопка хелп1
@dp.callback_query(F.data == "help1")
async def help(callback: CallbackQuery):
    await callback.message.answer("Ось що я вмію:\n/start - привітання👍\n/help - довідка✉️\n/quiz - міні вікторина👨‍🎓\n/about - про мене👌\n/joke - анекдот😂\n/bye - прощання🖐 \nА також я вмію обробляти звичайний текст,\nпросто напиши мені: Привіт, Як справи, Дякую, Анекдот, Історія тощо😊")
    await callback.answer()
#Кнопка хто створив
@dp.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    await callback.message.answer("️Я був створений Бобухом Богданом📑")
    await callback.answer()
#кнопка цікавий факт
@dp.callback_query(F.data == "fact")
async def about(callback: CallbackQuery):
    await callback.message.answer("️Чернівці - це єдине місто в Україні, де університет (ЧНУ) внесений до списку спадщини ЮНЕСКО!🎨.")
    await callback.answer()
#кнопка графік роботи
@dp.callback_query(F.data == "graphik")
async def about(callback: CallbackQuery):
    await callback.message.answer("️Мій графік:\nПрацюю 24/7🚀\nОхороняю твої дані👮‍♂️\nШифрую чати🔎")
    await callback.answer()


@dp.callback_query(F.data == "settings")
async def settings_handler(callback: CallbackQuery):

    settings_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Повернутися до меню", callback_data="start_menu")]
    ])

    await callback.message.edit_text(
        text=(
            "⚙️ **Параметри системи**\n\n"
            "Статус профілю: `Активний` ✅\n"
            "🔔 **Сповіщення:** `Увімкнено`\n"
            "🌐 **Мова інтерфейсу:** `Українська (UA)`\n\n"
            "--- --- --- --- ---\n"
            "🔹 **Технічна інформація:**\n"
            "• Версія бота: `1.0.4`\n"
            "• Локація: `Chernivtsi, UA`\n"
            "• ID сесії: `044-812`"
        ),
        reply_markup=settings_kb,
        parse_mode="Markdown"
    )
    await callback.answer()

#кнопка назад(повторка)
@dp.callback_query(F.data == "start_menu")
async def back_to_start(callback: CallbackQuery):

    kb = InlineKeyboardBuilder()
    kb.button(text="Скажи привіт🖐️", callback_data="say_hi")
    kb.button(text="Жарт😂", callback_data="joke")
    kb.button(text="Гід📑", callback_data="help1")
    kb.button(text="Хто створив🤞", callback_data="about")
    kb.button(text="Цікавий факт✨", callback_data="fact")
    kb.button(text="Графік роботи📈", callback_data="graphik")
    kb.button(text="Налаштування🔧", callback_data="settings")
    kb.adjust(1)

    await callback.message.edit_text(
        text="Вітаю! Я історичний бот на тематику Чернівців! \nНатисни кнопку нижче👇",
        reply_markup=kb.as_markup()
    )
    await callback.answer()
#--------------------------------------------команда хелп
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Ось що я вмію:\n/start - привітання👍\n/help - довідка✉️\n/quiz - міні вікторина👨‍🎓\n/about - про мене👌\n/joke - анекдот😂\n/bye - прощання🖐 \nА також я вмію обробляти звичайний текст,\nпросто напиши мені: Привіт, Як справи, Дякую, Анекдот, Історія тощо😊")

#команда about
@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("Я був створений Бобухом Богданом📑")

#команда joke
@dp.message(Command("joke"))
async def joke_command(message: Message):
    await message.answer("- Мамо, я хочу в Париж!\n - У нас є Париж вдома. \n Париж вдома: Чернівці, дощ, бруківка і пари в ЧНУ.")

#команда bye
@dp.message(Command("bye"))
async def bye_command(message: Message):
    await message.answer(f"Допобачення, {message.from_user.full_name}, гарного вам дня🖐️")


#команда quiz
@dp.message(Command("quiz"))
async def quiz_start(message: Message):
    kb = InlineKeyboardBuilder()

    kb.button(text="Ратуша", callback_data="quiz_wrong")
    kb.button(text="Університет (ЧНУ)", callback_data="quiz_correct")
    kb.button(text="Муздрамтеатр", callback_data="quiz_wrong")
    kb.button(text="Будинок-корабель", callback_data="quiz_wrong")
    kb.adjust(1)

    await message.answer(
        "📜 **Чернівецька вікторина:**\n\n"
        "Яка будівля в Чернівцях внесена до списку світової спадщини ЮНЕСКО?👨‍🏫",
        reply_markup=kb.as_markup(),
        parse_mode="Markdown"
    )

#правильна
@dp.callback_query(F.data == "quiz_correct")
async def quiz_yes(callback: CallbackQuery):
    await callback.message.edit_text(
        "Правильно! ✅\n\nЦе Резиденція митрополитів Буковини і Далмації (нині ЧНУ).",
        reply_markup=None
    )
    await callback.answer("Вітаю! +1 до знань 🎓")

#неправильна
@dp.callback_query(F.data == "quiz_wrong")
async def quiz_no(callback: CallbackQuery):
    await callback.answer("Спробуй ще раз! ❌", show_alert=True)

#-------------------------------------------------------обробка звичайного тексту
@dp.message()
async def echo_text(message: Message):
    text = message.text.lower()

    if "привіт" in text:
        await message.answer(f"Вітаю, {message.from_user.full_name}! 🖐️")
    elif "жарт" in text or "анекдот" in text:
        await message.answer(
            "- Мамо, я хочу в Париж!\n- У нас є Париж вдома. \nПариж вдома: Чернівці, дощ, бруківка і пари в ЧНУ.")
    elif "гід" in text or "що ти вмієш" in text:
        await message.answer("Ось що я вмію:\n/start - привітання👍\n/help - довідка✉️\n/quiz - міні вікторина👨‍🎓\n/about - про мене👌\n/joke - анекдот😂\n/bye - прощання🖐 \nА також я вмію обробляти звичайний текст,\nпросто напиши мені: Привіт, Як справи, Дякую, Анекдот, Історія тощо😊")
    elif "хто створив" in text or "автор" in text:
        await message.answer("Я був створений Бобухом Богданом 📑")
    elif "цікавий факт" in text:
        await message.answer(
            "Чернівці - це єдине місто в Україні, де університет (ЧНУ) внесений до списку спадщини ЮНЕСКО! 🎨")
    elif "графік" in text:
        await message.answer("Мій графік:\nПрацюю 24/7 🚀\nОхороняю твої дані 👮‍♂️")
    elif "вікторина" in text:
        await quiz_start(message)
    elif "допобачення" in text:
        await message.answer(f"Допобачення, {message.from_user.full_name}!")
    elif "дякую" in text:
        await message.answer("Будь ласка, був радий допомогти 🫡")
    else:
        await message.answer("Вибач, не зрозумів повідомлення. Спробуй скористатися кнопками меню! 😯")
# Запуск
async def main():
    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
#test