import telebot
from telebot import types

TOKEN = "8855322627:AAFgM_aeyMk2TRjUsORyIFx3azIY-enBjCQ"
ADMIN_ID = 8506271275
current_url = "https://grabify.link/MUBD3J"

bot = telebot.TeleBot(TOKEN)

def admin_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔗 Источник")
    keyboard.add(btn1)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == ADMIN_ID:
        bot.send_message(message.chat.id, "👑 Админ-панель:", reply_markup=admin_keyboard())
        return

    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 Запустить бота", web_app=types.WebAppInfo(current_url))
    markup.add(btn)

    caption = "Нажми кнопку, чтобы запустить бота."
    bot.send_message(message.chat.id, caption, reply_markup=markup, parse_mode='Markdown')

print("Бот успешно запущен!")
bot.infinity_polling()
