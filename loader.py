import os
from aiogram import Dispatcher, Bot, Router
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


dp = Dispatcher(storage=MemoryStorage())

bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
router = Router()