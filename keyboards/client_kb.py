from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")
ufc_button = KeyboardButton("/ufc")
basketball_button = KeyboardButton("/bball")
jdm_button = KeyboardButton("/jdm")


share_location = KeyboardButton("Share location", request_location=True)
share_contact = KeyboardButton("Share contact", request_contact=True)

start_markup.add(start_button, info_button, quiz_button,
                 share_location, share_contact, mem_button,
                 basketball_button, ufc_button, jdm_button)