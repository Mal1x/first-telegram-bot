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
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

class Order(StatesGroup):
    service_type = State()
    user_phone = State()

main_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="About"), KeyboardButton(text="/order")]],resize_keyboard=True)
phone_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Send Phone Number", request_contact = True)]], resize_keyboard=True,one_time_keyboard=True)
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="More info", callback_data="More_info")]])

@dp.callback_query(F.data == "More_info")
async def more_info(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer("Example of Inline button")

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer("Hello!", reply_markup=main_kb)

@dp.message(F.text == "About")
async def about(message: Message):
    await message.answer("This is a test bot.", reply_markup=inline_kb)

@dp.message(Command('order'))
async def form(message: Message, state: FSMContext):
    await state.set_state(Order.service_type)
    await message.answer("Which service do you want to use?")

@dp.message(Order.service_type)
async def process_service(message: Message, state: FSMContext):
    await state.update_data(service_type=message.text)

    await state.set_state(Order.user_phone)
    await message.answer("Write your phone number.", reply_markup=phone_kb)

@dp.message(Order.user_phone)
async def process_number(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
    if phone.isdigit() or message.contact:
        await state.update_data(user_phone=phone)
        data = await state.get_data()
        await state.clear()
        await message.answer(f"Finished!\nService: {data['service_type']}\nPhone Number: {data['user_phone']}")
    else:
        await message.answer("Write your phone number.", reply_markup=phone_kb)
        await state.set_state(Order.user_phone)


@dp.message()
async def text(message: Message):
    await message.answer(f"You wrote: {message.text}")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':  asyncio.run(main())