from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="About"), KeyboardButton(text="/order")]],resize_keyboard=True)
phone_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Send Phone Number", request_contact = True)]], resize_keyboard=True,one_time_keyboard=True)
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="More info", callback_data="More_info")]])
