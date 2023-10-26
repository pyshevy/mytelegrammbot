from aiogram import types
from keyboards.kb_inline.inline_kb import (
    START_MENU
)

async def start(message: types.Message) -> None:
    await message.answer(text=f'Здравствуйте, {message.from_user.full_name}! Выберите нужный пункт из меню ниже', reply_markup=START_MENU)