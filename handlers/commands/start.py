from aiogram import types, Router, F
from aiogram.types import CallbackQuery

from keyboards.kb_inline.inline_kb import (
    START_MENU
)

async def start(call_data: CallbackQuery) -> None:
    print(call_data.data)
    await call_data.message.answer(text=f'Здравствуйте ! Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
