from aiogram.types import BotCommand

bot_command: tuple = (
    ('start', 'For starting bot'),
)


async def set_command(bot) -> None:
    command: list = []
    for cmd in bot_command:
        command.append(BotCommand(command=cmd[0], description=cmd[1]))

    await bot.set_my_commands(command)