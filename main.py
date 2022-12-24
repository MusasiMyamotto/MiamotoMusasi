from aiogram.utils import executor
from handlars import client, callback, extra, add_func, admin, fsmAdminMentor, notification
from config import dp
import logging
from database.bot_db import sql_create
import asyncio


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
add_func.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)

extra.register_handler_extra(dp)


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
