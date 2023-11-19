from aiogram.fsm.state import StatesGroup, State


class States_class(StatesGroup):
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
    waiting_id_app = State()
    waiting_id_app_2 = State()