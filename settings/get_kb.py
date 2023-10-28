import asyncio
from typing import Union

from aiogram.types import InlineKeyboardButton
from random import shuffle, randint
from datetime import date, timedelta, datetime

from database import get_short_info_appointments, get_info_appointments, get_user_names


def create_kb() -> list:
    def get_date(day: int):
        today = date.today()
        date_ = f'{today.day}.{today.month}.{today.year}'
        dt = datetime.strptime(date_, '%d.%m.%Y')
        result = dt + timedelta(days=day)
        return result.strftime('%d.%m')

    inline_keyboard = [
        [
            InlineKeyboardButton(text=(a := f'Понедельник {get_date(1)} в {randint(9, 13)}:{randint(10, 50)}'),
                                 callback_data=a),
        ],
        [
            InlineKeyboardButton(text=(b := f'Вторник {get_date(2)} в {randint(9, 13)}:{randint(10, 50)}'),
                                 callback_data=b),
        ],
        [
            InlineKeyboardButton(text=(c := f'Среда {get_date(3)} в {randint(9, 13)}:{randint(10, 50)}'),
                                 callback_data=c),
        ],
        [
            InlineKeyboardButton(text=(d := f'Четверг {get_date(4)} в {randint(9, 13)}:{randint(10, 50)}'),
                                 callback_data=d),
        ],
        [
            InlineKeyboardButton(text=(g := f'Пятница {get_date(5)} в {randint(9, 13)}:{randint(10, 50)}'),
                                 callback_data=g),
        ],
        [
            InlineKeyboardButton(text=(h := f'Суббота {get_date(6)} в {randint(9, 13)}:{randint(10, 50)}'),
                                 callback_data=h),
        ]
    ]

    my_list_days = inline_keyboard
    shuffle(my_list_days)
    shuffle(my_list_days)

    my_list_days = [my_list_days[i] for i in range(randint(2, 5) + 1)]

    result = sorted(my_list_days,
                    key=lambda x: ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'].index(
                        x[0].text.split(' ')[0]))

    return result


def get_kb_with_url(url, message_id, chat_id):
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Перейти в диалог", url=url),
        ],
        [
            InlineKeyboardButton(text="Ошибка исправлена!", callback_data=f'error-fixed-{message_id}_{chat_id}'),
        ],
        [
            InlineKeyboardButton(text="Удалить сообщение", callback_data=f"delete_{message_id}"),
        ]
    ]

    return inline_keyboard


async def get_kb_appointments(id: Union[str, int]) -> list:
    dates = await get_short_info_appointments(id=id)
    inline_keyboard = [[InlineKeyboardButton(text=date[0], callback_data=date[1])] for date in dates]
    return inline_keyboard

async def get_kb_with_names(id: Union[str, int]) -> list:
    kb = []
    names = await get_user_names(id=id)

    for name in names:
        if [InlineKeyboardButton(text=name, callback_data=name)] not in kb:
            kb.append([InlineKeyboardButton(text=name, callback_data=name)])

    kb.append([InlineKeyboardButton(text="-------", callback_data=" ")])
    kb.append([InlineKeyboardButton(text="🧳В меню🧳", callback_data="menu")])

    return kb