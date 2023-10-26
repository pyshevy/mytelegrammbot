from datetime import date as date_
import re


def normalizerd_date(data: dict) -> dict:
    date = data['date']

    today = date_.today()

    date = date.split('.')

    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= today.year:
        ...
    else:
        data['success'] = 'None'
        return data

    age = today.year - year - ((today.month, today.day) < (month, day))

    if age < 0:
        data['success'] = 'None'
        return data

    elif age < 1:
        age = today.month - month - (today.day < day)
        if age == 1:
            data['year'] = '1 месяц'
        elif age in [2,3,4]:

            data['year'] = f'{age} месяца'
        else:

            data['year'] = f'{age} месяцев'

    elif age == 1:
        data['year'] = '1 год'

    elif age in [2, 3, 4]:
        data['year'] = f'{age} года'

    else:
        data['year'] = f'{age} лет'

    return data