# Задание 2 - Импортируй нужные классы
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    @property
    def get_real_name(self):
            return self.__text
            
    def gen_markup(self):
        # Задание 3 - Создай метод для генерации Inline клавиатуры
        markup = 0 #'Клавиатуру'
        markup.row_width = 0 #получаем количество ответов

        for i, option in enumerate(quiz_questions):
                markup.add(InlineKeyboardButton(self.options, callback_data='correct'))
        else:
            markup.add(InlineKeyboardButton(self.options, callback_data='wrong'))

# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми")
]
