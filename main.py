from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging
import random


TOKEN = config("TOKEN")


bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам алейкум брат {message.from_user.first_name}")
    await message.answer("This is an answer method")
    await message.reply("This is a reply method")


@dp.message_handler(commands=['quiz'])
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
        open_period=15,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Сколько серий в самом длинном аниме"
    answers = [
        "720",
        "1020",
        "8450",
        "7056",
        "8934",
        "2350",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="по идее это сложно",
        open_period=15,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 3", callback_data="button_call_3")
    markup.add(button_call_1)

    question = "Как зовут этого персонажа "
    answers = [
        'Чосо',
        'Итадори',
        'Саске',
        'Джостер',
        'Gigachad',
    ]

    photo = open("media/images (9).jpeg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="",
        open_period=15,
        reply_markup=markup
    )

@dp.callback_query_handler(text="button_call_3")
async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 4", callback_data="button_call_4")
    markup.add(button_call_1)

    question = "А его как зовут"
    answers = [
        'Путин',
        'Майкл Джэксон',
        'Акыл',
        'КАЧОК',
        'Дуэйн Скала Джонсон',
    ]

    photo = open("media/Без названия (1).jpeg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="",
        open_period=15,
        reply_markup=markup,
    )


@dp.callback_query_handler(text="button_call_4")
async def quiz_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 5", callback_data="button_call_5")
    markup.add(button_call_1)

    question = "Кто изображён на этом логотипе"
    answers = [
        'Коби Брайнт',
        'Майкл Джордан',
        'Шакиил Онил',
        'Джерри Уэст',
        'Джордан Килгенон',
    ]

    photo = open("media/images.png", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="",
        open_period=15,
        reply_markup=markup,
    )


@dp.callback_query_handler(text="button_call_5")
async def quiz_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 6", callback_data="button_call_6")
    markup.add(button_call_1)

    question = "Чей шаринган"
    answers = [
        'Итачи',
        'Мадара',
        'Саске',
        'Арай',
        'Какаши',
        'Шисуи',
    ]

    photo = open("media/300px-ShisuiMangekyouSharingan.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="",
        open_period=15,
        reply_markup=markup,
    )


@dp.callback_query_handler(text="button_call_6")
async def quiz_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 7", callback_data="button_call_7")
    markup.add(button_call_1)

    question = "В каком фильме играли эти актёры"
    answers = [
        'Война бесконечности',
        'Час пик',
        'Крид',
        'Джанго освобождённый',
        'Война миров Z',
        'Шпион по соседству',
    ]

    photo = open("media/Без названия (5).jpeg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="",
        open_period=15,
        #reply_markup=markup,
    )





@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photos = (
        'media/images(9).jpeg',
        'media/images (10).jpeg',
        'media/images (11).jpeg',
        'media/images (12).jpeg',
        'media/images (13).jpeg',
        'media/images (14).jpeg',
        'media/images (15).jpeg',
        'media/images (16).jpeg',
        'media/images (17).jpeg',
        'media/images (18).jpeg',
        'media/images (19).jpeg',
        'media/images (20).jpeg',
        'media/images (21).jpeg',
        'media/images (22).jpeg',
        'media/images (23).jpeg',
        'media/Без названия (1).jpeg',
        'media/Без названия (2).jpeg',
        'media/Без названия (3).jpeg',
        'media/1aa9928b963e3bfbcf99546260f89847.jpeg',
        'media/1cuEOLZGsYZodTSEG9UMtQLAXCY.jpg',
        'media/flat,750x,075,f-pad,750x1000,f8f8f8.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
         await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)