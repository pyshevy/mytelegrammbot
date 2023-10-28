from typing import Union

import aiosqlite
import asyncio

async def create_db():
    async with aiosqlite.connect('database.db') as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            ID INTEGER,
            `NAME` TEXT,
            `DATE` TEXT, 
            OTDELENIE VARCHAR(20),
            DOCTOR_TYPE VARCHAR(50),
            DOCTOR_NAME TEXT,
            CABINET VARCHAR(5),
            `YEAR` VARCHAR(20),
            DATE_WRITTING VARCHAR(50),
            ID_WRITTING VARCHAR(20)      
        )""")

        await db.commit()

async def create_user(data: dict):
    id = int(data['id'])
    name = data['name']
    date = data['date']
    otdelenie = data['otdelenie']
    doctor_type = data['doctor'][0]
    doctor_name = data['doctor'][1]
    cabinet = data['doctor'][3]
    date_writting = data['date_a']
    year = data['year']
    id_writting = data['number']

    data_ = [id, name, date, otdelenie, doctor_type, doctor_name, cabinet, date_writting, year, id_writting]
    async with aiosqlite.connect('database.db') as db:
        await db.execute('INSERT INTO users(ID, NAME, DATE, OTDELENIE, DOCTOR_TYPE, DOCTOR_NAME, CABINET, DATE_WRITTING, YEAR, ID_APPOINTMENT) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data_)
        await db.commit()


# asyncio.run(create_user({'id': 1234, 'type': 'writing', 'otdelenie': 'Взрослая поликлиника', 'doctor': ['Врач невролог', 'Бичев Сергей Юрьевич', '10:00-14:00', '408'], 'name': 'Швейкин Иван Андреевич', 'date': '17.05.2008', 'year': '15 лет', 'date_a': 'Пятница 32.10 в 11:37', 'number': '354847'}))

async def get_user_appointments(id: Union[int, str]) -> list[tuple]:
    returned_data = []
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("""SELECT * FROM users WHERE id = ?""", [id]) as cursor:
            async for row in cursor:
                returned_data.append(row)

    return returned_data

async def get_short_info_appointments(id: Union[int, str]) -> list[tuple]:
    returned_data = []
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("""SELECT DATE_WRITTING, ID_APPOINTMENT date FROM users WHERE id = ?""", [id]) as cursor:
            async for row in cursor:
                returned_data.append(row)

    return returned_data

# print(asyncio.run(get_short_info_appointments(1158687926)))

async def get_info_appointments(id_app: Union[str, int]) -> list:
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("""SELECT * FROM users WHERE ID_APPOINTMENT = ?""", [id_app]) as cursor:
            async for row in cursor:
                returned_data = row

    return returned_data


# print(asyncio.run(get_info_appointments(292284)))

async def get_user_names(id: Union[int, str]) -> list[tuple]:
    returned_data = []
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("""SELECT name, `date` FROM users WHERE id = ?""", [id]) as cursor:
            async for row in cursor:
                returned_data.append(' '.join(row))
                # returned_data.append(row)

    return returned_data

# print(asyncio.run(get_user_names(1158687926)))


async def delete_user_appointment(id_appointment: Union[int, str], id: Union[str, int]) -> None:
    async with aiosqlite.connect('database.db') as db:
        await db.execute("DELETE FROM users WHERE ID = ? and ID_APPOINTMENT = ?", [id, id_appointment])
        await db.commit()

# asyncio.run(delete_user_appointment(id_appointment=354568, id=1234))