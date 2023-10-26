from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

START_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Запись на прием", callback_data="writing"),
            InlineKeyboardButton(text="Информация о больнице", callback_data="info"),
        ]
    ],
)

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