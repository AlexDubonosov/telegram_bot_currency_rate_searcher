
"""
Данный модуль запускает бот
"""

from loader import bot
import handlers
from telebot.custom_filters import StateFilter
from units.menu import menu
from database.models import create_models


if __name__ == '__main__':
    create_models()
    bot.add_custom_filter(StateFilter(bot))
    menu(bot)
    bot.infinity_polling()
