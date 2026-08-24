import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import user, order
from database.db import init_db

async def main():
    await init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        user.router,
        order.router
    )

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())