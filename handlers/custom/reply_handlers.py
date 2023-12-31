"""
Модуль для обработки полученного текста
"""


from telebot.types import ReplyKeyboardRemove, Message

from loader import bot
from states.user_state import MyStates


@bot.message_handler(func=lambda message: message.text == 'Нет, выбрать заново.')
def handle_remove_keyboard_or_start_date_choice(message: Message) -> None:
    """
    Функция при получении текста 'Нет, выбрать заново.' устанавливает состояние next_date и предлагает
     выбрать даты для построения графика заново.

    :param message:
    :return:
    """
    remove_keyboard = ReplyKeyboardRemove()
    bot.set_state(message.from_user.id, MyStates.next_date, message.chat.id)
    if message.text == 'Нет, выбрать заново.':
        bot.send_message(message.chat.id, 'Начните заново: /currency', reply_markup=remove_keyboard)
