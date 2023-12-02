from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings.get_kb import create_kb

LIST_DOCTOR_BIG = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Врач травматолог", callback_data="травматолог"),
        ],
        [
            InlineKeyboardButton(text="Терапевт-участковый", callback_data="терапевт"),
        ],
        [
            InlineKeyboardButton(text="Врач инфекционист", callback_data="инфекционист"),
        ],
        [
            InlineKeyboardButton(text="Врач офтальмолог", callback_data="офтальмолог"),
        ],
        [
            InlineKeyboardButton(text="Врач психотерапевт", callback_data="психотерапевт"),
        ],
        [
            InlineKeyboardButton(text="Врач невролог", callback_data="невролог"),
        ],
        [
            InlineKeyboardButton(text="Врач дерматовенеролог", callback_data="дерматовенеролог"),
        ],
        [
            InlineKeyboardButton(text="Врач оторино-ларинголог", callback_data="оторино-ларинголог"),
        ],
        [
            InlineKeyboardButton(text="Зубной врач", callback_data="зубной"),
        ],
        [
            InlineKeyboardButton(text="Врач уролог", callback_data="уролог"),
        ],
        [
            InlineKeyboardButton(text="⬅️Выбор отделения⬅️", callback_data="input_hospital"),
        ]
    ],
)

LIST_DOCTOR_KIDS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Педиатр-участковый", callback_data="педиатр_kid"),
            InlineKeyboardButton(text="Зубной врач", callback_data="зубной_kid"),
        ],
        [
            InlineKeyboardButton(text="⬅️Выбор отделения⬅️", callback_data="input_hospital"),
        ]
    ],
)

LIST_HOSPITAL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Взрослая поликлиника", callback_data="big"),
            InlineKeyboardButton(text="Детская поликлиника", callback_data="kids"),
        ],
        [
            InlineKeyboardButton(text="⬅️Выход⬅️", callback_data="menu"),
        ]
    ],
)


def hospitals():
    builder = InlineKeyboardBuilder()
    builder.row(*[
        InlineKeyboardButton(text="Взрослая поликлиника", callback_data="big"),
        InlineKeyboardButton(text="Детская поликлиника", callback_data="kids"),
        InlineKeyboardButton(text="⬅️Выход⬅️", callback_data="menu")
    ],
        width=2
    )

    return builder.as_markup()


def start_menu():
    builder = InlineKeyboardBuilder()
    builder.row(*[
            InlineKeyboardButton(text="Запись на прием", callback_data="writing"),
            InlineKeyboardButton(text="Мои записи", callback_data="my_app"),
            InlineKeyboardButton(text="Информация", callback_data="info")
        ],
        width=3
    )

    return builder.as_markup()


def info():
    builder = InlineKeyboardBuilder()
    builder.row(*[
            InlineKeyboardButton(text="O больнице", callback_data="info_hospital"),
            InlineKeyboardButton(text="O врачах", callback_data="info_doctors"),
            InlineKeyboardButton(text="Закрыть", callback_data="menu")
        ],
        width=1
    )

    return builder.as_markup()

EXIT = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="В меню", callback_data="menu"),
        ]
    ],
)

EXIT_for_conf = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="В меню", callback_data="menu_conf"),
        ]
    ],
)

DATE = InlineKeyboardMarkup(
    inline_keyboard=create_kb(),
)

CONF = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Подтверждаю✅", callback_data="OK"),
        ],
        [
            InlineKeyboardButton(text="❌Отмена❌", callback_data="menu"),
        ],
    ],
)

ERROR_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍💻Написать главному разработчику (CEO)👨‍💻", url='https://t.me/pyshevy'),
        ],
        [
            InlineKeyboardButton(text="🧳В меню🧳", callback_data="menu"),
        ],
    ],
)

INPUT_APP = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Выбор записи⬅️", callback_data='menu_app'),
        ],
        [
            InlineKeyboardButton(text="📄Талон📄", callback_data='get_talon'),
        ],
        [
            InlineKeyboardButton(text="🧳В меню🧳", callback_data="menu_app_2"),
        ],
    ],
)


class Pagination(CallbackData, prefix='pag'):
    action: str
    page: int


def paginator(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='⬅️', callback_data=Pagination(action='prev', page=page).pack()),
        InlineKeyboardButton(text='➡️', callback_data=Pagination(action='next', page=page).pack()),
        InlineKeyboardButton(text='🚫Закрыть🚫', callback_data=Pagination(action='close', page=page).pack()),
        width=2
    )

    return builder.as_markup()