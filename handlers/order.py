from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards.reply import phone_kb
from database.db import add_order

router = Router()

class Order(StatesGroup):
    service_type = State()
    user_phone = State()

@router.message(Command('order'))
async def form(message: Message, state: FSMContext):
    await state.set_state(Order.service_type)
    await message.answer("Which service do you want to use?")

@router.message(Order.service_type)
async def process_service(message: Message, state: FSMContext):
    await state.update_data(service_type=message.text)

    await state.set_state(Order.user_phone)
    await message.answer("Write your phone number.", reply_markup=phone_kb)

@router.message(Order.user_phone)
async def process_number(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
    if phone.isdigit() or message.contact:
        await state.update_data(user_phone=phone)
        data = await state.get_data()
        await state.clear()

        # Saving data to db
        await add_order(
            user_id=message.from_user.id,
            service_type=data['service_type'],
            user_phone=data['user_phone']
        )

        await message.answer(
            f"Order saved to DB!\nService: {data['service_type']}\nPhone Number: {data['user_phone']}"
        )
    else:
        await message.answer("Write your phone number.", reply_markup=phone_kb)
        await state.set_state(Order.user_phone)