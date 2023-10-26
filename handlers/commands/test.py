import os
import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, ErrorEvent
from aiogram.types import FSInputFile

from config import INFO
from keyboards.kb_inline.inline_kb import LIST_HOSPITAL, EXIT, START_MENU, LIST_DOCTOR_BIG, CONF, \
    LIST_DOCTOR_KIDS, EXIT_for_conf, ERROR_KB
from pdfs.states import create_pdf
from settings.get_kb import create_kb, get_kb_with_url
from config import OTDELENIE_DICT, DOCTORS_DICT
from settings.normalised_data import normalizerd_date


class OrderFood(StatesGroup):
    waiting_type = State()
    waiting_info = State()
    waiting_hospital = State()
    waiting_otdelenie = State()
    waiting_doctor = State()
    waiting_time = State()
    waiting_name = State()
    waiting_date = State()
    waiting_good_date = State()
    waiting_confirmation = State()
    waiting_admin = State()

router = Router()


@router.message(Command("start"))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(text=f'Здравствуйте, {message.from_user.full_name}! Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
    # Устанавливаем пользователю состояние "выбирает название"
    await state.set_state(OrderFood.waiting_type)


@router.callback_query(OrderFood.waiting_type)
async def food_chosen(call_data: CallbackQuery, state: FSMContext):
    if call_data.data == 'writing':
        await call_data.message.edit_text('Выберите отделение', reply_markup=LIST_HOSPITAL)
        await state.set_state(OrderFood.waiting_otdelenie)
        await state.update_data(type=call_data.data)
        await call_data.answer()

    elif call_data.data == 'info':
        await call_data.message.edit_text(INFO, reply_markup=EXIT)
        await state.clear()
        await state.set_state(OrderFood.waiting_info)

@router.callback_query(OrderFood.waiting_info)
async def food_cho_incorrectly(call_data: CallbackQuery, state: FSMContext):
    print(call_data.data)
    if call_data.data == 'menu':
        await state.clear()
        await call_data.message.edit_text(text=f'Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
        await state.set_state(OrderFood.waiting_type)

@router.callback_query(OrderFood.waiting_otdelenie)
async def food_chosen_incorrectly(call_data: CallbackQuery, state: FSMContext):
    if call_data.data in ['big', 'kids']:
        if call_data.data == 'big':
            await call_data.message.edit_text(f'Вы выбрали {OTDELENIE_DICT[call_data.data]}. Выберите специалиста', reply_markup=LIST_DOCTOR_BIG)

        elif call_data.data == 'kids':
            await call_data.message.edit_text(f'Вы выбрали {OTDELENIE_DICT[call_data.data]}. Выберите специалиста',
                                              reply_markup=LIST_DOCTOR_KIDS)

        await state.update_data(otdelenie=OTDELENIE_DICT[call_data.data])
        await state.set_state(OrderFood.waiting_doctor)
    elif call_data.data == 'menu':
        await state.clear()
        await call_data.message.edit_text(text=f'Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
        await state.set_state(OrderFood.waiting_type)


@router.callback_query(OrderFood.waiting_doctor)
async def food_size_chosen(call_data: CallbackQuery, state: FSMContext):

    if call_data.data == 'input_hospital':
        await call_data.message.edit_text('Выберите отделение', reply_markup=LIST_HOSPITAL)
        await state.set_state(OrderFood.waiting_otdelenie)
        await state.update_data(type=call_data.data)
        await call_data.answer()
    else:
        await call_data.message.edit_text(f'Вы выбрали: {DOCTORS_DICT[call_data.data][0]}.\nВаш врач: {DOCTORS_DICT[call_data.data][1]}\nКабинет: {DOCTORS_DICT[call_data.data][-1]}\n\nТеперь введите имя и дату рождения (Укажите в виде Имя Фамилия Отчество ДД.ММ.ГГГГ)', reply_markup=EXIT)
        await state.update_data(doctor=DOCTORS_DICT[call_data.data])
        await state.set_state(OrderFood.waiting_name)

@router.callback_query(OrderFood.waiting_name)
async def go_menu(call_data: CallbackQuery, state: FSMContext):
    if call_data.data == 'menu':
        await state.clear()
        await call_data.message.edit_text(text=f'Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
        await state.set_state(OrderFood.waiting_type)

@router.message(OrderFood.waiting_name)
async def get_name(msg: Message, state: FSMContext):
    name = ' '.join(msg.text.split(' ')[:-1])
    date = msg.text.split(' ')[-1]
    kb = create_kb()
    user_data = await state.get_data()
    new_data = normalizerd_date({'date': date})

    if not new_data.get('success') == 'None':
        await state.update_data(name=name, date=date, year=new_data['year'])
        ###---------------------------###
        ###---------------------------###
        await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id-1)
        ###---------------------------###
        ###---------------------------###
        await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        await msg.answer(f'Ваше отделение: {user_data["otdelenie"]}\nВаш врач: {user_data["doctor"][1]}\nКабинет: {user_data["doctor"][-1]}\n\nВаше ФИО: {name}\nВаша дата рождения: {date} ({new_data["year"]})\n\nВрач принимает {user_data["doctor"][2]}, выберите доступное окно', reply_markup= InlineKeyboardMarkup(inline_keyboard=kb))
        await state.set_state(OrderFood.waiting_date)
    else:
        # await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id-1)
        await state.update_data(name=name)
        await msg.bot.edit_message_text(chat_id=msg.chat.id, text=f'Вы ввели неверную дату рождения! Введите еще раз (формат ДД.ММ.ГГГГ). При повторном неверном вводе Вы отправитесь в меню!\n<b>Введите только дату рождения!</b>', reply_markup=EXIT, message_id=msg.message_id-1, )
        await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        await state.set_state(OrderFood.waiting_good_date)

@router.message(OrderFood.waiting_good_date)
async def date(msg: Message, state: FSMContext):
    date = msg.text
    new_data = normalizerd_date({'date': date})
    user_data = await state.get_data()


    if not new_data.get('success') == 'None':
        kb = create_kb()
        await state.update_data(date=date, year=new_data['year'])
        await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id - 2)
        await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        await msg.answer(f'Ваше отделение: {user_data["otdelenie"]}\nВаш врач: {user_data["doctor"][1]}\nКабинет: {user_data["doctor"][-1]}\n\nВаше ФИО: {user_data["name"]}\nВаша дата рождения: {date} ({new_data["year"]})\n\nВрач принимает {user_data["doctor"][2]}, выберите доступное окно', reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))
        await state.set_state(OrderFood.waiting_date)

    else:
        await state.clear()
        await msg.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        await msg.bot.edit_message_text(chat_id=msg.chat.id, text=f'Выберите нужный пункт из меню ниже', reply_markup=START_MENU, message_id=msg.message_id - 2)
        # await msg.edit_text(text=f'Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
        await state.set_state(OrderFood.waiting_type)

@router.callback_query(OrderFood.waiting_date)
async def food_size_chosen(call_data: CallbackQuery, state: FSMContext):
    await call_data.answer()
    user_data = await state.get_data()
    await state.update_data(date_a=f"{call_data.data}")
    await call_data.message.edit_text(f'Ваше отделение: {user_data["otdelenie"]}\nВаш врач: {user_data["doctor"][1]}\nКабинет: {user_data["doctor"][-1]}\n\nВаше имя: {user_data["name"]}\nВаша дата рождения: {user_data["date"]}\n\nВы будете записаны на {call_data.data}', reply_markup=CONF)
    await state.set_state(OrderFood.waiting_confirmation)

@router.callback_query(OrderFood.waiting_confirmation)
async def food_sizeosen(call_data: CallbackQuery, state: FSMContext):
    if call_data.data == 'OK':
            user_data = await state.get_data()
            id = random.randint(100001, 999999)
            create_pdf(data=user_data, id=id)
            await call_data.message.delete()
            filename = f'{id}.png'
            photo = FSInputFile(filename)
            await call_data.message.answer_photo(photo=photo, caption=f'Принято! Вы записаны на прием!\n\nИнформация о записи:\nВаше отделение: {user_data["otdelenie"]}\nВаш врач: {user_data["doctor"][1]}\nКабинет: {user_data["doctor"][-1]}\n\nВы записаны на {user_data["date_a"]}\n\nВаш талон прикреплен к сообщению!', reply_markup=EXIT_for_conf)
            await call_data.answer()
            os.remove(filename)

    elif call_data.data == 'menu_conf':
        await call_data.message.delete_reply_markup()
        await state.clear()
        await call_data.message.answer(text=f'Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
        await state.set_state(OrderFood.waiting_type)

    elif call_data.data == 'menu':
        await call_data.message.delete()
        await state.clear()
        await call_data.message.answer(text=f'Выберите нужный пункт из меню ниже', reply_markup=START_MENU)
        await state.set_state(OrderFood.waiting_type)


@router.error()
async def error_handlers(event: ErrorEvent, state: FSMContext):
    if event.update.callback_query:
        await event.update.callback_query.answer()
        user_id = event.update.callback_query.from_user.id
        message = event.update.callback_query.message
        chat_id = event.update.callback_query.message.chat.id
        message_id = event.update.callback_query.message.message_id
    else:
        user_id = event.update.message.from_user.id
        message = event.update.message
        chat_id = event.update.message.chat.id
        message_id = event.update.message.message_id

    await message.bot.edit_message_text(text='🛠 Произошла ошибка на стороне сервера! Приносим свои извинения! Данные об ошибке уже были переданы техническому отделу, скоро все будет работать! Попробуйте повторно записаться, при повторной ошибке пробуйте позже! 🛠', message_id=message_id - 1, chat_id=chat_id, reply_markup=ERROR_KB)
    text = f"""
    <b>[ERROR]</b>
    ID: {user_id}
    STATE: {await state.get_state()}
    STATE_DATA: {await state.get_data()}
    URL: {event.update.message.from_user.url}
    FULL_NAME: {event.update.message.from_user.full_name}
    \n
    ERROR_TEXT = {event.exception}
    <b>[ERROR]</b>
    """
    kb = get_kb_with_url(url=event.update.message.from_user.url, message_id=event.update.message.message_id, chat_id=event.update.message.chat.id)
    await message.delete()
    await message.bot.send_message(chat_id=os.environ.get('ADMIN_ID'), text=text, reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))


@router.callback_query()
async def recognase(call_data: CallbackQuery, state: FSMContext):
    print(call_data.data.split('_')[0].split('-')[-1])
    if call_data.data.startswith('error-fixed'):
        await call_data.message.bot.delete_message(chat_id=int(call_data.data.split('_')[1]), message_id=int(call_data.data.split('_')[0].split('-')[-1])-1)
        await call_data.message.bot.send_message(chat_id=int(call_data.data.split('_')[1]), text='Пссс... Я по-секрету... Админ все починил! :)', reply_markup=EXIT)
        await state.set_state(OrderFood.waiting_name)
        await call_data.answer()

    elif call_data.data.startswith('delete'):
        await call_data.message.delete()