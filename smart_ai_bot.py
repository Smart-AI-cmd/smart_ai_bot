
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Токены
BOT_TOKEN = "7560643091:AAGznh89E8LfHMkhP7mM15__9tbNXU9BF2Y"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

# Инициализация памяти и роли
user_memory = {}
default_role = "Ты дружелюбный AI-помощник, который даёт полезные советы."

# Функция смены роли
async def setrole(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    role_text = " ".join(context.args)
    if role_text:
        user_memory[user_id] = {"role": role_text, "history": []}
        await update.message.reply_text(f"✅ Роль установлена: {role_text}")
    else:
        await update.message.reply_text("Пожалуйста, укажи роль. Пример:
/setrole Ты маркетолог, который помогает писать офферы.")

# Основной чат
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_input = update.message.text

    if user_id not in user_memory:
        user_memory[user_id] = {"role": default_role, "history": []}

    memory = user_memory[user_id]["history"]
    role = user_memory[user_id]["role"]

    # Формируем запрос с памятью
    messages = [{"role": "system", "content": role}]
    for msg in memory[-5:]:  # последние 5 сообщений
        messages.append(msg)
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )

    reply = response.choices[0].message.content

    # Сохраняем диалог
    user_memory[user_id]["history"].append({"role": "user", "content": user_input})
    user_memory[user_id]["history"].append({"role": "assistant", "content": reply})

    await update.message.reply_text(reply)

# Запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("setrole", setrole))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
