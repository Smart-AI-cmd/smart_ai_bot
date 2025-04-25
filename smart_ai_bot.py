
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

script = {
    "1_первичное_касание": "Привет! 👋 Я Smart_AI ассистент.\nПомогаю автоматизировать рутину и зарабатывать через ИИ.\nВыбери, что хочешь сделать:",
    "2_прогрев": "С чем ты чаще сталкиваешься в продвижении?\n✅ Мало контента?\n✅ Нужен системный подход?\n✅ Хочешь, чтобы за тебя подумали?",
    "3_оффер": "У меня есть система Smart_AI. За 3 дня ты запустишь продукт и сможешь зарабатывать 100–500$/день. Скинуть старт-пак?",
    "7_закрытие_лидмагнит": "Кидаю тебе PDF с инструкцией. Откроешь — увидишь, как легко стартануть.",
    "8_закрытие_оплата": "Хочешь сразу оплатить участие и получить персонального ассистента? Готов скинуть ссылку."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Получить PDF", callback_data="get_pdf")],
        [InlineKeyboardButton("Прогрев", callback_data="warmup")],
        [InlineKeyboardButton("Оффер", callback_data="offer")],
        [InlineKeyboardButton("Оплата", callback_data="pay")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(script["1_первичное_касание"], reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "get_pdf":
        await query.edit_message_text(text=script["7_закрытие_лидмагнит"])
    elif query.data == "warmup":
        await query.edit_message_text(text=script["2_прогрев"])
    elif query.data == "offer":
        await query.edit_message_text(text=script["3_оффер"])
    elif query.data == "pay":
        await query.edit_message_text(text=script["8_закрытие_оплата"])

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
