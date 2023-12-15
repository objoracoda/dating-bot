from aiogram.dispatcher.filters.state import StatesGroup, State


class states_match(StatesGroup):
    state_search_match = State()
    state_last_likes = []
    cur_like_profile = ''
