from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=5
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")
ufc_button = KeyboardButton("/ufc")
basketball_button = KeyboardButton("/bball")
jdm_button = KeyboardButton("/jdm")
reg_button = KeyboardButton("/reg")
anime_button = KeyboardButton("/anime")
wheel_button = KeyboardButton("/wheels")



share_location = KeyboardButton("Share location", request_location=True)
share_contact = KeyboardButton("Share contact", request_contact=True)

start_markup.add(start_button, info_button, quiz_button,
                 share_location, share_contact, mem_button,
                 basketball_button, ufc_button, jdm_button,
                 reg_button, anime_button, wheel_button)



cancel_button = KeyboardButton('CANCEL')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)

gender_m = KeyboardButton("Мужчина")
gender_f = KeyboardButton("Женщина")
gender_u = KeyboardButton("Незнаю")

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(gender_m, gender_f, gender_u, cancel_button)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))