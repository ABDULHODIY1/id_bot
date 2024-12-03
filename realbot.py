from aiogram import types,Dispatcher,Bot,executor
from dotenv import load_dotenv
import logging
import os
import sys
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
API_TOKEN = os.getenv("ID_BOT_TOKEN")  # <-- Yangi tokeningizni .env faylida belgilashingiz kerak

if not API_TOKEN:
    logger.error("❌ BOT_API_TOKEN o'zgaruvchisi topilmadi. Iltimos, .env faylini tekshiring.")
    sys.exit(1)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def info(msg:types.Message):
    await msg.answer(f"Your Info:\nID: {msg.from_user.id}\nUser name: {msg.from_user.username}")

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)