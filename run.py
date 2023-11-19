import asyncio
import os

from database import create_db
from loader import bot, dp
# from handlers import router_test
from settings.set_bot_command import set_command
from handlers import router, router_


async def run() -> None:

    if not os.path.isfile('database.db'):
        await create_db()

    dp.include_router(router_)
    dp.include_router(router)

    await set_command(bot)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Bot started!')
        asyncio.run(run())
    except KeyboardInterrupt:
        print('Bot stopped!')
