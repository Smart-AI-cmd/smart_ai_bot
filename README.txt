
Render деплой: как запустить Telegram-бота

1. Перейди на https://render.com → New → Web Service
2. Загрузи этот архив .zip на шаге создания
3. Настройки:
   - Environment: Python 3.10
   - Build Command: pip install -r requirements.txt
   - Start Command: python smart_ai_bot.py
4. Добавь переменную окружения:
   - Key: BOT_TOKEN
   - Value: твой Telegram токен
