from aiogram import types, Dispatcher
from config import bot, dp
import random



@dp.message_handler(commands=['bball'])
async def basketball(message: types.Message):
    photos = (
        'media/photo_2022-12-11_23-52-42.jpg',
        'media/photo_2022-12-11_23-52-45.jpg',
        'media/photo_2022-12-11_23-52-46.jpg',
        'media/photo_2022-12-11_23-52-47.jpg',
        'media/photo_2022-12-11_23-52-48.jpg',
        'media/photo_2022-12-11_23-52-49.jpg',
        'media/photo_2022-12-11_23-52-50.jpg',
        'media/photo_2022-12-11_23-52-52.jpg',
        'media/photo_2022-12-11_23-52-53.jpg',
        'media/photo_2022-12-11_23-52-54.jpg',
        'media/photo_2022-12-11_23-52-55.jpg',
        'media/photo_2022-12-11_23-52-56.jpg',
        'media/photo_2022-12-11_23-52-57.jpg',
        'media/photo_2022-12-11_23-52-59.jpg',
        'media/photo_2022-12-11_23-53-00.jpg',
        'media/photo_2022-12-11_23-53-01.jpg',
        'media/photo_2022-12-11_23-53-03.jpg',
        'media/photo_2022-12-11_23-53-04.jpg',
        'media/photo_2022-12-11_23-53-05.jpg',
        'media/photo_2022-12-11_23-53-06.jpg',
        'media/photo_2022-12-11_23-53-07.jpg',
        'media/photo_2022-12-11_23-53-08.jpg',
        'media/photo_2022-12-11_23-53-09.jpg',
        'media/photo_2022-12-11_23-53-10.jpg',
        'media/photo_2022-12-11_23-53-11.jpg',
        'media/photo_2022-12-11_23-53-12.jpg',
        'media/photo_2022-12-11_23-53-13.jpg',
        'media/photo_2022-12-11_23-53-14.jpg',
        'media/photo_2022-12-11_23-53-15.jpg',
        'media/photo_2022-12-11_23-53-16.jpg',
        'media/photo_2022-12-11_23-53-18.jpg',
        'media/photo_2022-12-11_23-53-19.jpg',
        'media/photo_2022-12-11_23-53-20.jpg',
        'media/photo_2022-12-11_23-53-22.jpg',
        'media/photo_2022-12-11_23-53-24.jpg',
        'media/photo_2022-12-11_23-53-25.jpg',
        'media/photo_2022-12-11_23-53-26.jpg',
        'media/photo_2022-12-11_23-53-27.jpg',
        'media/photo_2022-12-11_23-53-28.jpg',
        'media/photo_2022-12-11_23-53-29.jpg',
        'media/photo_2022-12-11_23-53-30.jpg',
        'media/photo_2022-12-11_23-53-32.jpg',
        'media/photo_2022-12-11_23-53-33.jpg',
        'media/photo_2022-12-11_23-53-34.jpg',
        'media/photo_2022-12-11_23-53-35.jpg',
        'media/photo_2022-12-11_23-53-36.jpg',
        'media/photo_2022-12-11_23-53-37.jpg',
        'media/photo_2022-12-11_23-53-38.jpg',
        'media/photo_2022-12-11_23-53-39.jpg',
        'media/photo_2022-12-11_23-53-40.jpg',
        'media/photo_2022-12-11_23-53-41.jpg',
        'media/photo_2022-12-11_23-53-42.jpg',
        'media/photo_2022-12-11_23-53-43.jpg',
        'media/photo_2022-12-11_23-53-44.jpg',
        'media/photo_2022-12-11_23-53-45.jpg',
        'media/photo_2022-12-11_23-53-46.jpg',
        'media/photo_2022-12-11_23-53-47.jpg',
        'media/photo_2022-12-11_23-53-48.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


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
        'media/photo_2022-12-10_20-45-40.jpg',
        'media/photo_2022-12-10_20-45-42.jpg',
        'media/photo_2022-12-10_20-45-45.jpg',
        'media/photo_2022-12-10_20-45-46.jpg',
        'media/photo_2022-12-10_20-45-47.jpg',
        'media/photo_2022-12-10_20-45-48.jpg',
        'media/photo_2022-12-10_20-45-49.jpg',
        'media/photo_2022-12-10_20-45-50.jpg',
        'media/photo_2022-12-10_20-45-51.jpg',
        'media/photo_2022-12-10_20-45-52.jpg',
        'media/photo_2022-12-10_20-45-54.jpg',
        'media/photo_2022-12-10_20-45-57.jpg',
        'media/photo_2022-12-10_20-45-58.jpg',
        'media/photo_2022-12-10_20-46-00.jpg',
        'media/photo_2022-12-10_20-46-02.jpg',
        'media/photo_2022-12-10_21-04-06.jpg',
        'media/photo_2022-12-10_21-04-08.jpg',
        'media/photo_2022-12-10_21-04-10.jpg',
        'media/photo_2022-12-10_21-04-11.jpg',
        'media/photo_2022-12-10_21-04-12.jpg',
        'media/photo_2022-12-10_21-04-13.jpg',
        'media/photo_2022-12-10_21-04-15.jpg',
        'media/photo_2022-12-10_21-04-16.jpg',
        'media/photo_2022-12-10_00-46-49.jpg',
        'media/photo_2022-12-11_16-17-10.jpg',
        'media/photo_2022-12-11_16-17-30.jpg',
        'media/photo_2022-12-11_16-18-00.jpg',
        'media/photo_2022-12-11_16-18-12.jpg',
        'media/photo_2022-12-11_16-18-32.jpg',
        'media/photo_2022-12-11_16-18-54.jpg',
        'media/photo_2022-12-11_16-18-58.jpg',
        'media/photo_2022-12-11_16-19-21.jpg',
        'media/photo_2022-12-11_16-30-58.jpg',
        'media/photo_2022-12-11_16-31-00.jpg',
        'media/photo_2022-12-11_16-31-01.jpg',
        'media/photo_2022-12-11_16-31-02.jpg',
        'media/photo_2022-12-11_16-31-03.jpg',
        'media/photo_2022-12-11_16-31-05.jpg',
        'media/photo_2022-12-11_16-31-07.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
         await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)

def register_handlers_callback(dp: Dispatcher):
    dp.register_message_handler(basketball, commands=['bball'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(echo, commands=['math'])
