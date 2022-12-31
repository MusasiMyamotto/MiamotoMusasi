from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random

from parser_wheel.wheel import ParserWheels




async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам алейкум брат {message.from_user.first_name}",
                                reply_markup=start_markup)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Когда выпустили первую серию аниме Наруто"
    answers = [
        '2 февраля 2003',
        '4 октября 2002',
        '12 марта 2002',
        '3 октября 2002',
        '23 февраля 2003 ',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        #open_period=15,
        reply_markup=markup
    )


async def info_handler(message: types.Message):
    await message.reply("Сам рабирайся!")

async def dice_game(message: types.Message):
    bot_dice = await bot.send_dice(message.chat.id)
    user_dice = await bot.send_dice(message.chat.id)
    await message.answer("первый игральный кость бота а второй игрока")
    if bot_dice.dice.value > user_dice.dice.value:
        await message.answer(f"Бот выиграл {message.from_user.full_name}!")
    elif bot_dice.dice.value == user_dice.dice.value:
        await message.answer("Ничья")
    else:
        await message.answer(f"{message.from_user.full_name} выиграл бота!")


async def get_random_user(message: types.Message):
    await sql_command_random(message)

async def parsser_wheels(message: types.Message):
    items = ParserWheels.parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['link']}"
            f"{item['logo']}\n"
            f"# {item['size']}\n"
            f"цена - {item['price']}\n"
            )




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(dice_game, commands=['dice'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(parsser_wheels, commands=['wheels'])