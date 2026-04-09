import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

API_TOKEN = "8569352099:AAG68TPFnYk97NHwQhp46PIJQmY1pDio6is"
dp=Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт я твій перший бот")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main))


