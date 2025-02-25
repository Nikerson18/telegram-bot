import logging
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "8109632757:AAHJDDDcfidBLLym_ZDYIu4bH001P1LkcKE"

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context) -> None:
    await update.message.reply_text("Привет! Я бот для учета зарплат и водителей.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()