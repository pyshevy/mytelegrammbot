from aiogram.types import InlineKeyboardButton
from random import shuffle, randint
from datetime import date

def create_kb() -> list:
    today = date.today()
    day = today.day
    inline_keyboard = [
        [
            InlineKeyboardButton(text=(a := f'Понедельник {day+2}.{today.month} в {randint(9, 13)}:{randint(10, 50)}'), callback_data=a),
        ],
        [
            InlineKeyboardButton(text=(b := f'Вторник {day+3}.{today.month} в {randint(9, 13)}:{randint(10, 50)}'), callback_data=b),
        ],
        [
            InlineKeyboardButton(text=(c := f'Среда {day+4}.{today.month} в {randint(9, 13)}:{randint(10, 50)}'), callback_data=c),
        ],
        [
            InlineKeyboardButton(text=(d := f'Четверг {day+5}.{today.month} в {randint(9, 13)}:{randint(10, 50)}'), callback_data=d),
        ],
        [
            InlineKeyboardButton(text=(g := f'Пятница {day+6}.{today.month} в {randint(9, 13)}:{randint(10, 50)}'), callback_data=g),
        ],
        [
            InlineKeyboardButton(text=(h := f'Суббота {day+7}.{today.month} в {randint(9, 13)}:{randint(10, 50)}'), callback_data=h),
        ]
    ]

    my_list_days = inline_keyboard
    shuffle(my_list_days)
    shuffle(my_list_days)

    my_list_days = my_list_days[randint(2, 5):]

    result = sorted(my_list_days, key=lambda x: ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'].index(x[0].text.split(' ')[0]))

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

