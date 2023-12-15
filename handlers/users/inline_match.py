from aiogram import types 
from aiogram.types import CallbackQuery

from aiogram.dispatcher import FSMContext

from loader import dp
from loader import db

from keyboards.inline import ikb_likes
from keyboards.default import kb_match_react, kb_reg

from states import states_match


@dp.message_handler(text='Показать Лайки')
async def send_likes(message: types.Message):
    await message.answer('Show inline',reply_markup=ikb_likes)


@dp.callback_query_handler(text="Показать Лайки")
async def send_random_value(call: CallbackQuery):
    try:
        states_match.state_last_likes = db.get_likes_data(call.from_user.id).split(';')
        states_match.cur_like_profile = db.get_user_data(states_match.state_last_likes[0])
        photo = open(states_match.cur_like_profile[5], 'rb')
        caption = (
                f'<b>{states_match.cur_like_profile[2]}</b>, {states_match.cur_like_profile[3]}\n'
                f'{states_match.cur_like_profile[6]}\n\n'
                f'{states_match.cur_like_profile[4]}\n\n')
        await dp.bot.send_photo(call.from_user.id, photo,caption=caption,reply_markup=kb_match_react)
        states_match.state_last_likes.remove(states_match.state_last_likes[0])
        await states_match.state_search_match.set()
        #await call.message.answer('Твоя анкета кому-то понравилась!'+str(likes_id))
    except IndexError:
        await call.message.answer('Лайков пока нет!',reply_markup=kb_reg)


@dp.message_handler(state=states_match.state_search_match)
async def match_state(message: types.Message, state: FSMContext):
    try:
        if message.text == '❤️':
            #await dp.bot.send_message(states_match.cur_like_profile[1],'Match! Взаимная симпатия!\n\nМожете начинать общаться - tg://openmessage?user_id=='+str(states_match.cur_like_profile[1]))
            await message.answer('Это однозначно Match, можете начинать общаться!\n\ntg://openmessage?user_id=='+str(states_match.cur_like_profile[1]))

            states_match.cur_like_profile = db.get_user_data(states_match.state_last_likes[0])
            photo = open(states_match.cur_like_profile[5], 'rb')
            caption = (
                f'<b>{states_match.cur_like_profile[2]}</b>, {states_match.cur_like_profile[3]}\n'
                f'{states_match.cur_like_profile[6]}\n\n'
                f'{states_match.cur_like_profile[4]}\n\n')
            await dp.bot.send_photo(message.from_user.id, photo,caption=caption,reply_markup=kb_match_react)
            states_match.state_last_likes.remove(states_match.state_last_likes[0])
            await states_match.state_search_match.set()
        else:
            states_match.cur_like_profile = db.get_user_data(states_match.state_last_likes[0])
            photo = open(states_match.cur_like_profile[5], 'rb')
            caption = (
                f'<b>{states_match.cur_like_profile[2]}</b>, {states_match.cur_like_profile[3]}\n'
                f'{states_match.cur_like_profile[6]}\n\n'
                f'{states_match.cur_like_profile[4]}\n\n')
            await dp.bot.send_photo(message.from_user.id, photo,caption=caption,reply_markup=kb_match_react)
            states_match.state_last_likes.remove(states_match.state_last_likes[0])
            await states_match.state_search_match.set()
    except IndexError:
        db.clear_likes(message.from_user.id)
        await message.answer('Пока лайки закончились, подождем пока кому-нибудь понравится твоя анкета!',reply_markup=kb_reg)
        await state.finish()
