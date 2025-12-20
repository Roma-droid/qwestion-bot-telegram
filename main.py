import telebot
from config import token
from collections import defaultdict  # ✅ Задание 7
from logic import quiz_questions

user_responses = defaultdict(int)     # можно тоже сделать defaultdict
points = defaultdict(int)             # ✅ Задание 8

bot = telebot.TeleBot(token)

def send_question(chat_id):
    bot.send_message(
        chat_id,
        quiz_questions[user_responses[chat_id]].text,
        reply_markup=quiz_questions[user_responses[chat_id]].gen_markup()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        points[chat_id] += 1            # ✅ Задание 9
    elif call.data == "wrong":
        bot.answer_callback_query(call.id, "Answer is wrong")

    user_responses[chat_id] += 1        # ✅ Задание 5

    if user_responses[chat_id] >= len(quiz_questions):
        bot.send_message(
            chat_id,
            f"The end! Your score: {points[chat_id]}"  # ✅ Задание 6
        )
    else:
        send_question(chat_id)

@bot.message_handler(commands=['start'])
def start(message):
    send_question(message.chat.id)

bot.infinity_polling()