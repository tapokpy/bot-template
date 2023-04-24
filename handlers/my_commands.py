from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline import *


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")


@dp.message_handler(commands="help")
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку"
            )

    await message.answer("\n".join(text))


