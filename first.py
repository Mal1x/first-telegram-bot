import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Hello"), KeyboardButton(text="About")]],resize_keyboard=True)
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="More info", callback_data="More_info")]])

@dp.callback_query(F.data == "More_info")
async def more_info(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer("Example of Inline button")

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("Hello!", reply_markup=main_kb)

@dp.message(F.text == "Hello")
async def hello(message: Message):
    await message.answer("Hello")

@dp.message(F.text == "About")
async def about(message: Message):
    await message.answer("This is a test bot.", reply_markup=inline_kb)

@dp.message()
async def text(message: Message):
    await message.answer(f"You wrote: {message.text}")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':  asyncio.run(main())