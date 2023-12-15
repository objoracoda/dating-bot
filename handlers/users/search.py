from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType

from loader import dp
from loader import db

from utils.misc import rate_limit
from states import states_search
from keyboards.default import kb_search_react,kb_reg
from keyboards.inline import ikb_likes

import random


@dp.message_handler(text='🚀 Вперед')
async def command_start(message: types.Message):
    data_user = db.get_user_data(message.from_user.id)
    states_search.state_last_id = db.get_users_recommend(message.from_user.id,data_user[6],data_user[3],data_user[8])
    try:
        states_search.rec_user = random.choice(states_search.state_last_id)
        photo = open(states_search.rec_user[5], 'rb')
        caption = (
            f'<b>{states_search.rec_user[2]}</b>, {states_search.rec_user[3]}\n'
            f'{states_search.rec_user[6]}\n\n'
            f'{states_search.rec_user[4]}\n\n')
        await dp.bot.send_photo(message.chat.id, photo,caption=caption,reply_markup=kb_search_react)
        states_search.state_last_id.remove(states_search.rec_user)
        await states_search.state_search_reaction.set()
    except IndexError:
        await message.answer('Из твоего Города никого нет!\n\nУкажи другой город, чтобы искать там!')



@dp.message_handler(state=states_search.state_search_reaction)
async def register_state1(message: types.Message, state: FSMContext):
    try:
        if message.text == '❤️':
            #await message.answer('Ты лайкнул анкету!')
            if str(message.from_user.id) not in states_search.rec_user[9]:
                likes = states_search.rec_user[9]+';'+str(message.from_user.id)
                db.update_likes(states_search.rec_user[1],likes)
                #await dp.bot.send_message(states_search.rec_user[1],'Твоя анкета кому-то понравилась!',reply_markup=ikb_likes)
            states_search.rec_user = random.choice(states_search.state_last_id)
            photo = open(states_search.rec_user[5], 'rb')
            caption = (
                f'<b>{states_search.rec_user[2]}</b>, {states_search.rec_user[3]}\n'
                f'{states_search.rec_user[6]}\n\n'
                f'{states_search.rec_user[4]}\n\n')
            await dp.bot.send_photo(message.chat.id, photo,caption=caption,reply_markup=kb_search_react)
            states_search.state_last_id.remove(states_search.rec_user)
            await states_search.state_search_reaction.set()
        elif message.text == '💔':
            #await message.answer('Тебе не понравилась анкета!')
            states_search.rec_user = random.choice(states_search.state_last_id)
            photo = open(states_search.rec_user[5], 'rb')
            caption = (
                f'<b>{states_search.rec_user[2]}</b>, {states_search.rec_user[3]}\n'
                f'{states_search.rec_user[6]}\n\n'
                f'{states_search.rec_user[4]}\n\n')
            await dp.bot.send_photo(message.chat.id, photo,caption=caption,reply_markup=kb_search_react)
            states_search.state_last_id.remove(states_search.rec_user)
            await states_search.state_search_reaction.set()
        elif message.text == '💤':
            await message.answer('Будем искать анкеты в другой раз!',reply_markup=kb_reg)
            await state.finish()
    except IndexError:
        print('Start get profiles again!')
        data_user = db.get_user_data(message.from_user.id)
        states_search.state_last_id = db.get_users_recommend(message.from_user.id,data_user[6],data_user[3],data_user[8])
        states_search.rec_user = random.choice(states_search.state_last_id)

        photo = open(states_search.rec_user[5], 'rb')
        caption = (
            f'<b>{states_search.rec_user[2]}</b>, {states_search.rec_user[3]}\n'
            f'{states_search.rec_user[6]}\n\n'
            f'{states_search.rec_user[4]}\n\n')
        await dp.bot.send_photo(message.chat.id, photo,caption=caption,reply_markup=kb_search_react)
        states_search.state_last_id.remove(states_search.rec_user)
        await states_search.state_search_reaction.set()