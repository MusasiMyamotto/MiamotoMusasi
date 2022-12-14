from aiogram import types, Dispatcher
from config import bot
from config import ADMINS
import random


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")

async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        data = ['⚽️', '🏀', '🎯', '🎰', '🎳', '🎲']
        r = random.choice(data)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(message.chat.id, 'Ты не админ')

async def pin_message(message :types.Message):
    if message.reply_to_message and message.from_user.id in ADMINS:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await  message.answer("ты не админ")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(game, commands=['game'])