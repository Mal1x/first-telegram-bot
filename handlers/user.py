from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.reply import main_kb, inline_kb

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer("Hello!", reply_markup=main_kb)

@router.message(F.text == "About")
async def about(message: Message):
    await message.answer("This is a test bot.", reply_markup=inline_kb)

@router.callback_query(F.data == "More_info")
async def more_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Example of Inline button")