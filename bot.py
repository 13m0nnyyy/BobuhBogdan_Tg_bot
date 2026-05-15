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


#вікторина
@dp.message(Command("quiz"))
async def quiz_start(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Ратуша", callback_data="q1_wrong")
    kb.button(text="Університет (ЧНУ)", callback_data="q1_correct")
    kb.button(text="Муздрамтеатр", callback_data="q1_wrong")
    kb.button(text="Будинок-корабель", callback_data="q1_wrong")
    kb.adjust(1)

    await message.answer(
        "📜 **Чернівецька вікторина (Питання 1/3):**\n\n"
        "Яка будівля в Чернівцях внесена до списку світової спадщини ЮНЕСКО? 👨‍🏫",
        reply_markup=kb.as_markup(),
        parse_mode="Markdown"
    )


@dp.callback_query(F.data == "q1_wrong")
async def q1_no(callback: CallbackQuery):
    await callback.answer("Неправильно! Спробуй ще раз! ❌", show_alert=True)


@dp.callback_query(F.data == "q1_correct")
async def q1_yes(callback: CallbackQuery):
    await callback.answer("Правильно! +1 до знань 🎓")

    kb = InlineKeyboardBuilder()
    kb.button(text="Панська", callback_data="q2_correct")
    kb.button(text="Головна", callback_data="q2_wrong")
    kb.button(text="Руська", callback_data="q2_wrong")
    kb.button(text="Кобилянської", callback_data="q2_correct")
    kb.adjust(1)

    await callback.message.edit_text(
        "✅ **Чудово!**\n\n"
        "📜 **Чернівецька вікторина (Питання 2/3):**\n\n"
        "яку відому пішохідну вулицю Чернівців за австрійських часів підмітали букетами троянд? 🧹🌹",
        reply_markup=kb.as_markup(),
        parse_mode="Markdown"
    )


# питання 2
@dp.callback_query(F.data == "q2_wrong")
async def q2_no(callback: CallbackQuery):
    await callback.answer("Ні, цю вулицю мили звичайними швабрами. Спробуй іншу! ❌", show_alert=True)



@dp.callback_query(F.data == "q2_correct")
async def q2_yes(callback: CallbackQuery):
    await callback.answer("Її мили з милом і замітали трояндами!🌹")

    kb = InlineKeyboardBuilder()
    kb.button(text="Франц Йосиф I", callback_data="q3_correct")
    kb.button(text="Тарас Шевченко", callback_data="q3_wrong")
    kb.button(text="Міхай Емінеску", callback_data="q3_wrong")
    kb.adjust(1)

    await callback.message.edit_text(
        "🎉 **Фінальне питання:**\n\n"
        "📜 **вікторина (Питання 3/3):**\n\n"
        "Пам'ятник якому австрійському імператору за правління якого місто пережило 'золотий вік', встановлено у Чернівцях? 🏛️",
        reply_markup=kb.as_markup(),
        parse_mode="Markdown"
    )


#питання 3
@dp.callback_query(F.data == "q3_wrong")
async def q3_no(callback: CallbackQuery):
    await callback.answer("не вгадав!!", show_alert=True)


@dp.callback_query(F.data == "q3_correct")
async def q3_yes(callback: CallbackQuery):
    await callback.answer("ура! вікторину пройдено! 🥳")

    await callback.message.edit_text(
        "🏆 **Вітання! Ти пройшов всю вікторину!** ✅\n\n"
        "Ти чудово знаєш історію та архітектуру нашого міста!",
        reply_markup=None
    )
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