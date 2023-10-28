__all__ = ['router']

from aiogram import F

from .start import start
from .test import router





# ---------------------------------------* Register User Command *---------------------------------------#
# router.message.register(start, F.data == 'hello')