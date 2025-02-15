import asyncio
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, IMPORTANT_KEYWORDS

# Создаём объект бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Асинхронная функция для отправки уведомлений
async def send_notification(message):
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# Функция проверки важности запроса
def is_important_query(query):
    query_lower = query.lower()  # Приводим к нижнему регистру
    for keyword in IMPORTANT_KEYWORDS:
        if keyword in query_lower:
            return True
    return False

# Функция обработки важных запросов
def process_important_query(query):
    if is_important_query(query):
        message = f"⚠️ ВАЖНЫЙ ЗАПРОС: {query}"

        asyncio.run(send_notification(message)) 
