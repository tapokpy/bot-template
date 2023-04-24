from aiogram import executor

import handlers, keyboards, utils

from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)  # Устанавливаем дефолтные команды
    await on_startup_notify(dispatcher)  # Уведомляет админов про запуск


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
