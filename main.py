# -*- coding: utf-8 -*-

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Токен бота
TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Пример данных о водителях (можно заменить на базу данных или Google Sheets)
drivers_info = {
    "Иван Иванов": {"трак": "Volvo 2020", "телефон": "+1 123-456-7890"},
    "Петр Петров": {"трак": "Freightliner 2019", "телефон": "+1 987-654-3210"},
    "Эрдем": {"трак": "Scania 2021", "телефон": "+1 555-555-5555"}
}

# Функция для команды /start
async def start(update: Update, context) -> None:
    await update.message.reply_text(
        "Привет! Я BUDHMO_bot. Чем могу помочь? Для получения списка доступных команд, напишите /помощь."
    )

# Функция для команды /помощь
async def help_command(update: Update, context) -> None:
    await update.message.reply_text(
        "/помощь - Список команд\n"
        "/search_driver [имя] - Получить информацию о конкретном водителе\n"
        "/get_driver_info - Получить информацию о водителях\n"
        "/get_salary_report - Получить отчёт по зарплатам\n"
        "/send_document - Отправить документ"
    )

# Функция для отправки документа (например, PDF или изображения)
async def send_document(update: Update, context) -> None:
    file_path = 'путь_к_документу/документ.pdf'  # Укажи путь к документу
    try:
        with open(file_path, 'rb') as file:
            await update.message.reply_document(document=file)
    except FileNotFoundError:
        await update.message.reply_text("Документ не найден. Пожалуйста, проверьте путь к файлу.")

# Функция для получения информации о водителях
async def get_driver_info(update: Update, context) -> None:
    # Здесь можно добавить информацию о водителях (например, из базы данных или Google Sheets)
    driver_info = "Имя: Иван Иванов\nТрак: Volvo 2020\nТелефон: +1 123-456-7890"
    await update.message.reply_text(driver_info)

# Функция для поиска информации о конкретном водителе через текстовое сообщение
async def search_driver_by_message(update: Update, context) -> None:
    message_text = update.message.text.lower()  # Получаем текст сообщения и приводим к нижнему регистру
    if "водитель" in message_text:
        # Пытаемся найти имя водителя после слова "водитель"
        for driver_name in drivers_info:
            if driver_name.lower() in message_text:  # Сравниваем в нижнем регистре
                driver_info = drivers_info[driver_name]
                response = f"Имя: {driver_name}\nТрак: {driver_info['трак']}\nТелефон: {driver_info['телефон']}"
                await update.message.reply_text(response)
                return

        # Если имя водителя не найдено
        await update.message.reply_text("Водитель не найден. Пожалуйста, уточните имя.")
    else:
        await update.message.reply_text("Не могу найти информацию о водителе. Напишите 'водитель' и имя.")

# Функция для получения информации о всех водителях
async def get_all_drivers_info(update: Update, context) -> None:
    driver_list = "\n".join(drivers_info.keys())
    await update.message.reply_text(f"Список водителей:\n{driver_list}")

# Функция для получения отчёта по зарплатам
async def get_salary_report(update: Update, context) -> None:
    # Пример отчёта
    salary_report = "Зарплаты:\nДиспетчер 1: $3000\nДиспетчер 2: $3500\n..."
    await update.message.reply_text(salary_report)

# Главная функция, которая будет запускать бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("search_driver", get_driver_info))  # Команда для поиска водителя
    app.add_handler(CommandHandler("get_driver_info", get_driver_info))
    app.add_handler(CommandHandler("get_salary_report", get_salary_report))
    app.add_handler(CommandHandler("send_document", send_document))
    
    # Добавляем обработчик для текстовых сообщений, содержащих информацию о водителе
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_driver_by_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
