import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("Hello")

@dp.message()
async def text(message: Message):
    await message.answer(f"You wrote: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':  asyncio.run(main())