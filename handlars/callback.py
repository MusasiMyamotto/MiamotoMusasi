from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp

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
        #open_period=15,
        reply_markup=markup
    )



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
        #open_period=15,
        reply_markup=markup
    )


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
        #open_period=15,
        reply_markup=markup,
    )


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
        #open_period=15,
        reply_markup=markup,
    )


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
        #open_period=15,
        reply_markup=markup,
    )


async def quiz_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 8", callback_data="button_call_8")
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
        #open_period=15,
        reply_markup=markup,
    )


async def quiz_8(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 9", callback_data="button_call_9")
    markup.add(button_call_1)

    question = "Как думаешь мне нравится этот персонаж"
    answers = [
        'ДА',
        'НЕТ',
    ]

    photo = open("media/photo_2022-12-14_22-06-23.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="",
        #open_period=15,
        reply_markup=markup,
    )

async def quiz_9(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 10", callback_data="button_call_10")
    markup.add(button_call_1)

    question = "Расстояние от земли до Солнца"
    answers = [
        'без понятия',
        'лям км',
        '149 597 870 700 метров',
        '150 345 788 432 метров',
        '567 234 789 123 метров',
        'Ты шо дурак от куда мне знать',
    ]

    photo = open("media/Без названия (5).jpeg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="",
        #open_period=15,
        reply_markup=markup,
    )


async def quiz_10(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 11", callback_data="button_call_11")
    markup.add(button_call_1)

    question = "Какой самый лучший язык программирования?"
    answers = [
        'PHP',
        'Java',
        'JS',
        'Python',
        'Ruby',
        'C#',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="",
        #open_period=15,
        reply_markup=markup,
    )


async def quiz_11(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 12", callback_data="button_call_12")
    markup.add(button_call_1)

    question = "Кто лучший трансформер?"
    answers = [
        'Оптимус',
        'Рэтчет',
        'Мегатрон',
        'Сэнтинал',
        'Бамбл Би',
        'У меня не было счастливого детства',
    ]

    photo = open("media/photo_2022-12-14_22-25-03.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="",
        #open_period=15,
        reply_markup=markup,
    )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
    dp.register_callback_query_handler(quiz_4, text="button_call_3")
    dp.register_callback_query_handler(quiz_5, text="button_call_4")
    dp.register_callback_query_handler(quiz_6, text="button_call_5")
    dp.register_callback_query_handler(quiz_7, text="button_call_6")
    dp.register_callback_query_handler(quiz_8, text="button_call_7")
    dp.register_callback_query_handler(quiz_9, text="button_call_8")
    dp.register_callback_query_handler(quiz_10, text="button_call_9")
    dp.register_callback_query_handler(quiz_11, text="button_call_10")