from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, filters
import random
import asyncio


def get_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("Обо мне", callback_data='about')],
        [InlineKeyboardButton("Мои проекты", callback_data='projects')],
        [InlineKeyboardButton("Мой стэк технологий", callback_data='stack')],
        [InlineKeyboardButton("Получить произвищие", callback_data='get_ball')],
        [InlineKeyboardButton("Прочее", callback_data='more')],
        
    ]
    return InlineKeyboardMarkup(keyboard)

# /start
async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, "Ваш цифровой помощник от Zeta - к вашим услугам! 😊")
    await context.bot.send_message(chat_id, "Выбери, что хочешь узнать:", reply_markup=get_main_keyboard())
        
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'about':
        await query.message.reply_text("Name : Ernur\nAge : 17\nNick names : Zeta\nAbout me : Don't love JavaScript, I'm not friends with the frontend")
    elif query.data == 'projects':
        await query.message.reply_text("Мои проекты: \nTelegram-боты,\nвеб-приложения на Streamlit,\nБэкенд (Django,Flask),\nФишинг сайт(BackEnd), \nРутинная автоматизация, \nDDOS атака")
    elif query.data == 'stack':
        await query.message.reply_text("Python 3.12+ ,\nDjango,\nDRF,\nSQLite,\nAsyncio,\npython-telegram-bot,\nStreamlit,\nGitHub, \nBash, \nLinux, \nFlask")
    elif query.data == 'more':
        await query.message.reply_text("Частые вопросы: \n1. Какой у тебя любимый язык программирования? \n2. Какой у тебя любимый фреймворк? \n3. Какой у тебя любимый проект? \n4. Какой у тебя любимый хобби?")
    elif query.data == 'get_ball':
        await query.answer()  # Это отвечает на запрос callback
        await query.edit_message_text(random.choice(["Ты — Лох ! ", "Ты — Красава !  ", "Ты — Ниггер ! "]))


    # Отправить заново меню после ответа
    await query.message.reply_text("Выбери другой пункт:", reply_markup=get_main_keyboard())

# Обработка любого текста
async def echo(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if text == '1':
        await update.message.reply_text("У меня только 1 язык программирования, и это Python!")
    elif text == '2':
        await update.message.reply_text("Мой любимый фреймворк — Django!")
    elif text == '3':
        await update.message.reply_text("Мой любимый проект — это BackEnd сайта!")
    elif text == '4':
        await update.message.reply_text("Мое любимое хобби — это писать всякие говнокоды!")
    
import os

def main():
    TOKEN = "7203448075:AAEN5FI1dU7HraBMniOoqXex-AbYSYB8lu4"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "localhost:10000")

    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", "10000")),
        url_path=TOKEN,
        webhook_url=f"https://{hostname}/{TOKEN}"
    )

if __name__ == '__main__':
    main()
    