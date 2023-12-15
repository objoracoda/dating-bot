from aiogram.dispatcher.filters.state import StatesGroup, State


class states_search(StatesGroup):
    state_search_reaction = State()
    state_last_id = []
    rec_user = ''
