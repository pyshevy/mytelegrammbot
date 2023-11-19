__all__ = ['router', 'router_']

from aiogram import F, Router

from .start import start
from .test import router, info_doctors
from settings.states import States_class

router_ = Router()





# ---------------------------------------* Register User Command *---------------------------------------#
# router_.callback_query.register(info_doctors, F.data == 'info_doctors', States_class.waiting_type)