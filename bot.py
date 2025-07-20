
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توكن البوت
TOKEN = "7629738298:AAFezq4KjwKe26dG_snmGDbfLJfuE_GjL10"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("عرض شحن 1", callback_data="offer1"),
        InlineKeyboardButton("عرض شحن 2", callback_data="offer2")
    )
    bot.send_message(message.chat.id, "مرحباً بك في بوت الشحن 👋\nاختر أحد العروض التالية:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "offer1":
        bot.answer_callback_query(call.id, "🛒 تم اختيار عرض الشحن 1")
        bot.send_message(call.message.chat.id, "✅ تفاصيل عرض الشحن 1:\n- السعر: 5$\n- مدة التوصيل: فوري")
    elif call.data == "offer2":
        bot.answer_callback_query(call.id, "🛒 تم اختيار عرض الشحن 2")
        bot.send_message(call.message.chat.id, "✅ تفاصيل عرض الشحن 2:\n- السعر: 10$\n- مدة التوصيل: خلال 24 ساعة")

bot.infinity_polling()
