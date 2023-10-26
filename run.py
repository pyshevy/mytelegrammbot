import asyncio

from loader import bot, dp
from handlers import router_test
from settings.set_bot_command import set_command

async def run() -> None:

    #hellofisadk
    dp.include_router(router_test)

    await set_command(bot)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Bot started!')
        asyncio.run(run())
    except KeyboardInterrupt:
        print('Bot stopped!')
