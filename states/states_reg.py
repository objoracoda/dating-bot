from aiogram.dispatcher.filters.state import StatesGroup, State


class states_reg(StatesGroup):
    state_name = State()
    state_age = State()
    state_gender = State()
    state_photo = State()
    state_content = State()
    state_find_gender = State()
    state_city = State()