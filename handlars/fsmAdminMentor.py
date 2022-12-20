from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from keyboards.client_kb import submit_markup, cancel_markup
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.id.set()
        await message.answer(f"Здраствуй {message.from_user.full_name}")
        await message.answer("id ментора", reply_markup=cancel_markup)
    elif message.from_user.id not in ADMINS:
        await message.answer("ТЫ НЕ КУРАТОР!!!")
    else:
        await message.answer('Пиши в личку!')


async def load_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = int(message.text)

            await FSMAdmin.next()
            await message.answer("Как зовут?", reply_markup=cancel_markup)

    except:
        await bot.send_message(message.from_user.id, "id состоит только из цифр")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.from_user.id, "Какое направление?")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст", reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    try:
        if 50 > int(message.text) > 12:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Из какой группы?", reply_markup=cancel_markup)
        else:
            await message.answer("возраст не подходит")
    except:
        await message.answer("Вводи только числа!")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await bot.send_message(message.from_user.id, f"id - {data['id']},\n"
                                                     f"имя - {data['name']},\n"
                                                     f"направление - {data['direction']},\n"
                                                     f"возраст - {data['age']}, \n"
                                                     f"группа - {data['group']}")

    await FSMAdmin.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await bot.send_message(message.from_user.id, "Регистрация завершена")
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer('Не получилось!')




async def cancel_reg(message: types.Message, state: FSMContext):
    curren_state = await state.get_state()
    if curren_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты!")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')


    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)