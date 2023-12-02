import os
import random
from contextlib import suppress

from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, ErrorEvent, InlineKeyboardButton, \
    InputMediaPhoto
from aiogram.types import FSInputFile

from config import INFO
from keyboards.kb_inline.inline_kb import LIST_HOSPITAL, EXIT, start_menu, LIST_DOCTOR_BIG, CONF, \
    LIST_DOCTOR_KIDS, EXIT_for_conf, ERROR_KB, INPUT_APP, paginator, Pagination, info, hospitals
from pdfs.states import create_pdf
from settings.get_kb import create_kb, get_kb_with_url, get_kb_appointments, get_kb_with_names
from config import OTDELENIE_DICT, DOCTORS_DICT
from settings.normalised_data import normalizerd_date
from database import create_user, get_info_appointments, get_user_names
from settings.states import States_class

router = Router()

@router.callback_query(States_class.waiting_id_app)
async def food_cho_incorrectsaly(call_data: CallbackQuery, state: FSMContext):
    if call_data.data == 'go_menuu':
        await state.clear()
        await call_data.message.edit_text(text=f'Выберите нужный пункт из меню ниже', reply_markup=start_menu())
        await state.set_state(States_class.waiting_type)

    else:
        info = await get_info_appointments(id_app=call_data.data)
        # print(info)
        await call_data.message.edit_text(f"""ФИО: {info[1]}\n
Дата рождения: {info[2]} ({info[7]})\n
\n
Поликлиника: {info[3]}\n
Специалист: {info[4]}\n
Врач: {info[5]}\n
Номер кабинета: {info[6]}\n
\n
Дата записи: {info[8]}\n
Номер записи: {info[9]}\n
    """, reply_markup=INPUT_APP)
        await state.update_data(id_app=call_data.data)
        await state.set_state(States_class.waiting_id_app_2)
        await call_data.answer()


@router.callback_query(States_class.waiting_id_app_2)
async def food_cho_incorrectly(call_data: CallbackQuery, state: FSMContext):
    if call_data.data == 'menu_app':
        kb = await get_kb_appointments(id=call_data.from_user.id)
        if kb:
            kb.append([InlineKeyboardButton(text="🧳В меню🧳", callback_data='go_menuu')])
            await call_data.message.edit_text(
                'Выберите вашу запись и нажмите на нее для получения дополнительной информации',
                reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))
            await state.clear()
            await state.set_state(States_class.waiting_id_app)

    elif call_data.data == 'menu_app_2':
        await state.clear()
        await call_data.message.edit_text(text=f'Выберите нужный пункт из меню ниже', reply_markup=start_menu())
        await state.set_state(States_class.waiting_type)

    elif call_data.data == 'get_talon':
        user_data = await state.get_data()
        info = await get_info_appointments(id_app=user_data['id_app'])
        id = random.randint(100001, 999999)
        create_pdf(data={f'otdelenie': {info[3]}, 'doctor': [{info[4]}, {info[5]}, info[6]], 'name': {info[1]}, 'date': {info[2]}, 'year': {info[7]}, 'date_a': {info[8]}, 'number': {id}}, id=id)
        await call_data.message.delete()
        filename = f'{id}.png'
        photo = FSInputFile(filename)
        await call_data.message.answer_photo(photo=photo,
                                             caption=f'Ваш талон прикреплен к сообщению!',
                                             reply_markup=EXIT_for_conf)
        await call_data.answer()
        await state.set_state(States_class.waiting_confirmation)
        os.remove(filename)