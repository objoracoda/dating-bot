from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType

from loader import dp
from loader import db

from states import states_reg
from keyboards.default import kb_menu, kb_reg


@dp.message_handler(text='👤 Новая Анкета')
async def register(message: types.Message):
    from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

    name = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'{message.from_user.first_name}'),
        ],
    ],
    resize_keyboard = True)

    await message.answer('Отлично, составим новую Анкету!\n\nКак тебя зовут?',reply_markup=name)
    await states_reg.state_name.set()


@dp.message_handler(state=states_reg.state_name)
async def register_state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(state_name=answer)
    await message.answer(f'{answer}, сколько тебе лет?',reply_markup=None)
    await states_reg.state_age.set()


@dp.message_handler(state=states_reg.state_age)
async def register_state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(state_age=answer)

    from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

    genders = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я парень'),
            KeyboardButton(text='Я девушка'),
        ],
    ],
    resize_keyboard = True)

    await message.answer('Определимся с твоим полом 👀',reply_markup=genders)
    await states_reg.state_gender.set()


@dp.message_handler(state=states_reg.state_gender)
async def register_state3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(state_gender=answer)
    data = await state.get_data()
    name = data.get('state_name')
    await message.answer(f'{name}, пришли cвою самую классную фоточку 😍')
    await states_reg.state_photo.set()


@dp.message_handler(content_types=ContentType.PHOTO,state=states_reg.state_photo)
async def register_state4(message: types.Message, state: FSMContext):
    photos = message.photo
    destination_photo = 'media/users/'+str(message.from_user.id)+'.jpg'
    await photos[2].download(destination_file=destination_photo)
    await state.update_data(state_photo=destination_photo)

    data = await state.get_data()
    name = data.get('state_name')
    await message.answer(f'{name}, расскажи немного о себе!\n\nА исскуственный интеллект поможет подобрать тебе пару, на основе твоей анкеты 😉')
    await states_reg.state_content.set()


@dp.message_handler(state=states_reg.state_content)
async def register_state5(message: types.Message, state: FSMContext):
    from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

    gender_find = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Девушки'),
            KeyboardButton(text='Парни'),
            KeyboardButton(text='Не важно'),
        ],
    ],
    resize_keyboard = True)
    answer = message.text

    await state.update_data(state_content=answer)
    await message.answer('Кого ищем?',reply_markup=gender_find)
    await states_reg.state_find_gender.set()


@dp.message_handler(state=states_reg.state_find_gender)
async def register_state6(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(state_find_gender=answer)
    await message.answer('Из какого ты города?')
    await states_reg.state_city.set()


@dp.message_handler(state=states_reg.state_city)
async def register_state7(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(state_city=answer)
    data = await state.get_data()

    await message.answer(f'Анкета создана! Давай посмотрим на твой профиль 👀',reply_markup=kb_reg)
    db.add_user(message.from_user.id,
        data.get('state_name'),
        data.get('state_age'),
        data.get('state_gender'),
        data.get('state_photo'),
        data.get('state_content'),
        data.get('state_find_gender'),
        data.get('state_city'),
        'done')
    await state.finish()