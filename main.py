from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
import asyncio
import telegram.error

# Создаем Flask-приложение
app = Flask(__name__)
async def button_handler(update: Update, context):
    query = update.callback_query
    try:
        await query.answer()
    except telegram.error.BadRequest:
        pass


# 🔒 Список разрешённых пользователей (замени ID на реальные)
ALLOWED_USERS = {5538804267, 1430105405, 8026256981, 6932066810, 7275611563, 723670550, 5880565984, }  # Замени на свои ID

# 🔐 Функция проверки доступа
def check_access(update: Update) -> bool:
    user_id = update.effective_user.id
    if user_id not in ALLOWED_USERS:
        if update.message:
            update.message.reply_text("🚫 Доступ запрещён. Свяжитесь с администратором.")
        elif update.callback_query:
            update.callback_query.message.reply_text("🚫 Доступ запрещён.")
        return False
    return True

# Обработчик нажатия кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except telegram.error.BadRequest:
        pass

## 🚀 Функция /start и при определённых словах
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:  # Если это не текстовое сообщение, пропускаем
        return

    text = update.message.text.lower()  # Делаем текст сообщения строчными буквами

    trigger_words = ["привет", "hi", "Salut", "начать", "старт"]  # Список ключевых слов
    if update.message.text.startswith("/") or text in trigger_words:  # Проверяем команду или слова
        keyboard = [[InlineKeyboardButton("👥 Список диспетчеров", callback_data='dispatchers')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("🚛 Главное меню:", reply_markup=reply_markup)

# 🔄 Главное меню (пример)
def main_menu():
    keyboard = [[InlineKeyboardButton("📋 Список водителей", callback_data='drivers')]]
    return InlineKeyboardMarkup(keyboard)

# Данные (пока вручную)
dispatchers = {
    "🚛 Диспетчер Andrew": ["Водитель Ramil", "Водитель Mukhamed", "Водитель Adam (Oleg Reshaev)", "Водитель Oleh Semenenho"],
    "🚚 Диспетчер David": ["Водитель Inal", "Водитель Marat", "Водитель Azat", "Водитель Aleksei Lamathanov", "Водитель Aleksandr Pavlov"],
    "🚌 Диспетчер Serghei": ["Водитель Grigori", "Водитель Sergei Ciobanu", "Водитель Sergei Honcharenko"],
    "🚋 Диспетчер Vick": ["Водитель Darman", "Водитель Totraz", "Водитель Yerkebulan", "Водитель Mairbek", "Водитель Marin"],
    "🏍 Диспетчер Nick": ["Водитель Albert", "Водитель Vladimir", "Водитель Ashamaz"],
    "🚂 Диспетчер Peter": ["Водитель Tsyden", "Водитель Sultan", "Водитель Azat Azamat"],
    "🚀 Диспетчер Dima": ["Водитель Denis", "Водитель Aslanbek", "Водитель Georgii", "Водитель Igor"],
    "✈ Диспетчер Max": ["Водитель Erdem", "Водитель Said", "Водитель Dostan", "Водитель Dmitrii Kovarda"]

}

drivers_info = {
    "Водитель Ramil": (
        "📌 Информация о Ramil: \n"
        "📞 Phone Number: 916-282-8457 \n"
        "🚛 Truck Number: 34 \n"
        "🛻 Trailer Number: 34 \n"
        "🔑 VIN:3C6UR5KL2FG537458"
    ),
    "Водитель Mukhamed": (
        "📌 Информация о Mukhamed: \n"
        "📞 Phone Number: 224-474-0482 \n"
        "🚛 Truck Number: 3 \n"
        "🛻 Trailer Number: 3 \n"
        "🔑 VIN:3C63RRHL8RG307633"
    ),
    "Водитель Adam (Oleg Reshaev)": (
        "📌 Информация о Adam (Oleg Reshaev): \n"
        "📞 Phone Number: 279-789-4042 \n"
        "🚛 Truck Number: 23 \n"
        "🛻 Trailer Number: 23 \n"
        "🔑 VIN:3C63RRHL1RG289668"
    ),
    "Водитель Oleh Semenenho": (
        "📌 Информация о Oleh Semenenho: \n"
        "📞 Phone Number: 786-843-1879 \n"
        "🚛 Truck Number: 25 \n"
        "🛻 Trailer Number: 25 \n"
        "🔑 VIN:3C63RRHL2RG307630"
    ),
    "Водитель Inal": (
        "📌 Информация о Inal: \n"
        "📞 Phone Number: 708-969-9882 \n"
        "🚛 Truck Number: 24 \n"
        "🛻 Trailer Number: 24 \n"
        "🔑 VIN:3C63RRHL4RG289664 "
    ),
    "Водитель Marat": (
        "📌 Информация о Marat: \n"
        "📞 Phone Number: 754-280-7200 \n"
        "🚛 Truck Number: 14 \n"
        "🛻 Trailer Number: 14 \n"
        "🔑 VIN:3C63RRHL6RG289665 "
    ),
    "Водитель Azat": (
        "📌 Информация о Azat: \n"
        "📞 Phone Number:929 627 1722 \n"
        "🚛 Truck Number: 21 \n"
        "🛻 Trailer Number: 21 \n"
        "🔑 VIN:3C63RRGL3RG109933 "
    ),
    "Водитель Aleksei Lamathanov": (
        "📌 Информация о Aleksei Lamathanov: \n"
        "📞 Phone Number:323-219-9464 \n"
        "🚛 Truck Number: 10 \n"
        "🛻 Trailer Number: 10 \n"
        "🔑 VIN:3C63RRGL6RG109909 "
    ),
    "Водитель Aleksandr Pavlov": (
        "📌 Информация о Aleksandr Pavlov: \n"
        "📞 Phone Number:929-721-9669 \n"
        "🚛 Truck Number: 7 \n"
        "🛻 Trailer Number: 7 \n"
        "🔑 VIN:3C63RRHL4RG358188 "
    ),
    "Водитель Grigori": (
        "📌 Информация о Grigori: \n"
        "📞 Phone Number:754-284-6442 \n"
        "🚛 Truck Number: 15 \n"
        "🛻 Trailer Number: 15 \n"
        "🔑 VIN:3C63RRHL0RG280427 "
    ),
    "Водитель Serghei Ciobanu": (
        "📌 Информация о Serghei Ciobanu: \n"
        "📞 Phone Number:224-343-1680 \n"
        "🚛 Truck Number: 28 \n"
        "🛻 Trailer Number: 28 \n"
        "🔑 VIN:3C63RRHL5RG337088 "
    ),
    "Водитель Serghei Honcharenko": (
        "📌 Информация о Serghei Honcharenko: \n"
        "📞 Phone Number:386-225-1619 \n"
        "🚛 Truck Number: 19 \n"
        "🛻 Trailer Number: 19 \n"
        "🔑 VIN:3C63RRGL2RG219808 "
    ),
    "Водитель Darman": (
        "📌 Информация о Darman: \n"
        "📞 Phone Number:718-344-0617 \n"
        "🚛 Truck Number: 4 \n"
        "🛻 Trailer Number: 4 \n"
        "🔑 VIN:3C63RRHLXRG341413 "
    ),
    "Водитель Totraz": (
        "📌 Информация о Totraz: \n"
        "📞 Phone Number:754-286-7577 \n"
        "🚛 Truck Number: 16 \n"
        "🛻 Trailer Number: 16 \n"
        "🔑 VIN:3C63RRHL2PG643033 "
    ),
    "Водитель Yerkebulan": (
        "📌 Информация о Yerkebulan: \n"
        "📞 Phone Number:773-751-9292 \n"
        "🚛 Truck Number: 18 \n"
        "🛻 Trailer Number: 18 \n"
        "🔑 VIN:3C63RRHL0RG289662 "
    ),
    "Водитель Mairbek": (
        "📌 Информация о Mairbek: \n"
        "📞 Phone Number:925-497-0899 \n"
        "🚛 Truck Number: 32 \n"
        "🛻 Trailer Number: 32 \n"
        "🔑 VIN:3C63RRHL2RG289436 "
    ),
    "Водитель Marin": (
        "📌 Информация о Marin: \n"
        "📞 Phone Number:916-912-7398 \n"
        "🚛 Truck Number: 26 \n"
        "🛻 Trailer Number: 26 \n"
        "🔑 VIN:1GT49LEY8RF467913 "
    ),
    "Водитель Albert": (
        "📌 Информация о Albert: \n"
        "📞 Phone Number:347-739-8531 \n"
        "🚛 Truck Number: 22 \n"
        "🛻 Trailer Number: 22 \n"
        "🔑 VIN:3C63RRHL9KG642308 "
    ),
    "Водитель Vladimir": (
        "📌 Информация о Vladimir: \n"
        "📞 Phone Number:224-598-4179 \n"
        "🚛 Truck Number: 9 \n"
        "🛻 Trailer Number: 9 \n"
        "🔑 VIN:3C63RRGL2RG112628 "
    ),
    "Водитель Ashamaz": (
        "📌 Информация о Ashamaz: \n"
        "📞 Phone Number:551-755-0050 \n"
        "🚛 Truck Number: 17 \n"
        "🛻 Trailer Number: 17 \n"
        "🔑 VIN:3C63RRHL0RG341422 "
    ),
    "Водитель Tsyden": (
        "📌 Информация о Tsyden: \n"
        "📞 Phone Number:347-232-8827 \n"
        "🚛 Truck Number: 36 \n"
        "🛻 Trailer Number: 36 \n"
        "🔑 VIN:1FT8W3DT3REF83199 "
    ),
    "Водитель Sultan": (
        "📌 Информация о Sultan: \n"
        "📞 Phone Number:224-601-4124 \n"
        "🚛 Truck Number: 2 \n"
        "🛻 Trailer Number: 2 \n"
        "🔑 VIN:3C63RRHL2RG358187 "
    ),
    "Водитель Azat Azamat": (
        "📌 Информация о Azat Azamat: \n"
        "📞 Phone Number:253-286-8080 \n"
        "🚛 Truck Number: 29 \n"
        "🛻 Trailer Number: 29 \n"
        "🔑 VIN:3C63RRGL6RG382381 "
    ),
    "Водитель Denis": (
        "📌 Информация о Denis: \n"
        "📞 Phone Number:630-352-9196 \n"
        "🚛 Truck Number: 38 \n"
        "🛻 Trailer Number: 38 \n"
        "🔑 VIN:3C63RRHL6RG289522 "
    ),
    "Водитель Aslanbek": (
        "📌 Информация о Aslanbek: \n"
        "📞 Phone Number:845-674-4158 \n"
        "🚛 Truck Number: 33 \n"
        "🛻 Trailer Number: 33 \n"
        "🔑 VIN:3C63RRHL9RG301260 "
    ),
    "Водитель Georgii": (
        "📌 Информация о Georgii: \n"
        "📞 Phone Number:925-440-1503 \n"
        "🚛 Truck Number: 35 \n"
        "🛻 Trailer Number: 35 \n"
        "🔑 VIN:3C63RRGL0NG356465 "
    ),
    "Водитель Igor": (
        "📌 Информация о Igor: \n"
        "📞 Phone Number:331-229-8750 \n"
        "🚛 Truck Number: 20 \n"
        "🛻 Trailer Number: 20 \n"
        "🔑 VIN:3C63RRGL3KG618197 "
    ),
    "Водитель Erdem": (
        "📌 Информация о Erdem: \n"
        "📞 Phone Number:412-304-4565 \n"
        "🚛 Truck Number: 8 \n"
        "🛻 Trailer Number: 8 \n"
        "🔑 VIN:3C63R3GL6NG159989 "
    ),
    "Водитель Said": (
        "📌 Информация о Said: \n"
        "📞 Phone Number:305-391-1839 \n"
        "🚛 Truck Number: 6 \n"
        "🛻 Trailer Number: 6 \n"
        "🔑 VIN:3C63RRGL0RG183858 "
    ),
    "Водитель Dostan": (
        "📌 Информация о Dostan: \n"
        "📞 Phone Number:917-704-3848 \n"
        "🚛 Truck Number: 37 \n"
        "🛻 Trailer Number: 37 \n"
        "🔑 VIN:3C63RRHL6RG307632 "
    ),
    "Водитель Dmitrii Kovarda": (
        "📌 Информация о Dmitrii Kovarda: \n"
        "📞 Phone Number:213-716-3608 \n"
        "🚛 Truck Number: 12 \n"
        "🛻 Trailer Number: 12 \n"
        "🔑 VIN:3C63RRHL6RG341392 "
    ),
}

async def show_dispatchers(update: Update, context: CallbackQueryHandler):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in dispatchers.keys()]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='start')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("👥 Выберите диспетчера:", reply_markup=reply_markup)

async def show_drivers(update: Update, context: CallbackQueryHandler):
    query = update.callback_query
    selected_dispatcher = query.data
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in dispatchers[selected_dispatcher]]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='dispatchers')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(f"🚛 Водители диспетчера {selected_dispatcher}:", reply_markup=reply_markup)

async def show_driver_info(update: Update, context: CallbackQueryHandler):
    query = update.callback_query
    selected_driver = query.data
    keyboard = [
        [InlineKeyboardButton("📸 Фото", callback_data=f"photo_{selected_driver}"),
         InlineKeyboardButton("📂 Файлы", callback_data=f"files_{selected_driver}")],
        [InlineKeyboardButton("⬅️ Назад", callback_data='dispatchers')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text(f"{drivers_info[selected_driver]}", reply_markup=reply_markup)

async def button_handler(update: Update, context: CallbackQueryHandler):
    query = update.callback_query
    await query.answer()
    if query.data == 'start':
        await start(update, context)
    elif query.data == 'dispatchers':
        await show_dispatchers(update, context)
    elif query.data in dispatchers:
        await show_drivers(update, context)
    elif query.data in drivers_info:
        await show_driver_info(update, context)
    elif query.data.startswith("photo_") or query.data.startswith("files_"):
        await query.message.reply_text("📂 Функция загрузки пока не реализована.")

# Создание приложения
app = Application.builder().token("8109632757:AAHJDDDcfidBLLym_ZDYIu4bH001P1LkcKE").build()

# Добавление обработчиков
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    app.run_polling()
