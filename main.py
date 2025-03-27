from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import telegram.error

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


Dispatchers = {
    "🚛 Диспетчер Andrew": ["Водитель RAMIL KHAFIZOV", "Водитель OLEG RESHAEV", "Водитель OLEH SEMENENNKO", "Водитель MUKHAMED ADZHIEV"],
    "🚚 Диспетчер David": ["Водитель ALEKSEI LAMATKHANOV", "Водитель BAIR DABAIN", "Водитель MARAT KAZIEV", "Водитель AZAT BORONCHIEV", "Водитель MUKHAR KHUGAEV", "Водитель ALEKSANDR PAVLOV"],
    "🚌 Диспетчер Serghei": ["Водитель GHEORGHE BALICA", "Водитель SERGHEI CIOBANU", "Водитель SERHII HONCHARENKO"],
    "🚋 Диспетчер Vick": ["Водитель DARMAN ORUZBAEV", "Водитель TOTRAZ ABAEV", "Водитель YERKEBULAN BOSHAIBEKOV", "Водитель MAIRBEK KHASIGOV", "Водитель MARIN GULIA"],
    "🏍 Диспетчер Nick": ["Водитель ALBERT ABAIKHANOV", "Водитель ASKHABALI SHABANOV", "Водитель ILLIA HORBATOK"],
    "🚂 Диспетчер Peter": ["Водитель TSYDEN TOBODORZHIEV", "Водитель VIKTOR ATANOV", "Водитель AZAT AZAMAT"],
    "🚀 Диспетчер Dima": ["Водитель GEORGII RIONELI", "Водитель DENIS COLESNICENCO", "Водитель IGOR BALAKIN", "Водитель TAULAN TOTORKULOV"],
    "✈ Диспетчер Max": ["Водитель ERDEM DORZHIEV", "Водитель (Said) MAGOMEDSAID GABIBULAEV", "Водитель (DOS) DASTAN MASYLKANOV", "Водитель SOSLAN GAGLOEV"]

}

drivers_info = {
    "Водитель RAMIL KHAFIZOV": (
        "📌 Driver Name: RAMIL KHAFIZOV \n"
        "📞 Phone Number: 916-282-8457 \n"
        "🚛 Truck Number: 34 \n"
        "🚂 Trailer Number: 34 \n"
        "🔑 VIN:3C6UR5KL2FG537458 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Marin"
    ),
    "Водитель OLEH SEMENENNKO": (
        "📌 Driver Name: OLEH SEMENENNKO \n"
        "📞 Phone Number: 786-843-1879 \n"
        "🚛 Truck Number: 25 \n"
        "🚂 Trailer Number: 25 \n"
        "🔑 VIN:3C63RRHL2RG307630 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Radu",
    ),
    "Водитель OLEG RESHAEV": (
        "📌 Driver Name: OLEG RESHAEV \n"
        "📞 Phone Number: 279-789-4042 \n"
        "🚛 Truck Number: 23 \n"
        "🚂 Trailer Number: 23 \n"
        "🔑 VIN:3C63RRHL1RG289668 \n" 
        "⚓Ramps: 10ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Alex",
    ),
    "Водитель MUKHAMED ADZHIEV": (
        "📌 Driver Name: MUKHAMED ADZHIEV \n"
        "📞 Phone Number: 786-843-1879 \n"
        "🚛 Truck Number: 3 \n"
        "🚂 Trailer Number: 3 \n"
        "🔑 VIN:3C63RRHL8RG307633 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Dumitru Ou",
    ),
    "Водитель ALEKSEI LAMATKHANOV": (
        "📌 Driver Name: ALEKSEI LAMATKHANOV \n"
        "📞 Phone Number: 323-219-9464 \n"
        "🚛 Truck Number: 9 \n"
        "🚂 Trailer Number: 9 \n"
        "🔑 VIN:3C63RRGL2RG112628 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель MARAT KAZIEV": (
        "📌 Driver Name: MARAT KAZIEV \n"
        "📞 Phone Number: 754-280-7200 \n"
        "🚛 Truck Number: 14 \n"
        "🚂 Trailer Number: 14 \n"
        "🔑 VIN:3C63RRHL6RG289665 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Alex ",
    ),
    "Водитель AZAT BORONCHIEV": (
        "📌 Driver Name: AZAT BORONCHIEV \n"
        "📞 Phone Number: 929-627-1722 \n"
        "🚛 Truck Number: 21 \n"
        "🚂 Trailer Number: 21 \n"
        "🔑 VIN:3C63RRGL3RG109933 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Alexei Lamatkhanov ",
    ),
    "Водитель INAL VALIEV": (
        "📌 Driver Name: INAL VALIEV \n"
        "📞 Phone Number: 708-969-9882 \n"
        "🚛 Truck Number: 24 \n"
        "🚂 Trailer Number: 24 \n"
        "🔑 VIN:3C63RRHL4RG289664 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Alex ",
    ),
    "Водитель ALEKSANDR PAVLOV": (
        "📌 Driver Name: ALEKSANDR PAVLOV \n"
        "📞 Phone Number: 929-721-9669 \n"
        "🚛 Truck Number: 1 \n"
        "🚂 Trailer Number: 1 \n"
        "🔑 VIN:1GC4KTEY7SF130031 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель MUKHAR KHUGAEV": (
        "📌 Driver Name: MUKHAR KHUGAEV \n"
        "📞 Phone Number: 224-651-5069 \n"
        "🚛 Truck Number: 31 \n"
        "🚂 Trailer Number: 31 \n"
        "🔑 VIN:3C63RRJLLXNG152569 \n"
        "⚓Ramps: 10ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex ",
    ),
    "Водитель BAIR DABAIN": (
        "📌 Driver Name: BAIR DABAIN \n"
        "📞 Phone Number: 470-978-5585 \n"
        "🚛 Truck Number: 10 \n"
        "🚂 Trailer Number: 10 \n"
        "🔑 VIN:3C63RRGL6RG109909 \n"
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Alexei Lamatkhanov",
    ),
    "Водитель GHEORGHE BALICA": (
        "📌 Driver Name: GHEORGHE BALICA \n"
        "📞 Phone Number: 331-215-3466 \n"
        "🚛 Truck Number: 33 \n"
        "🚂 Trailer Number: 33 \n"
        "🔑 VIN:3C63RRHL9RG301260 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9620lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель SERGHEI CIOBANU": (
        "📌 Driver Name: SERGHEI CIOBANU \n"
        "📞 Phone Number: 224-343-1680 \n"
        "🚛 Truck Number: 28 \n"
        "🚂 Trailer Number: 28 \n"
        "🔑 VIN:3C63RRHL5RG337088 \n" 
        "⚓Ramps: 14ft \n"
        "⚖ Weight: 9220lb \n"
        "🅱 Owner: Dumitru OU ",
    ),
    "Водитель SERHII HONCHARENKO": (
        "📌 Driver Name: SERHII HONCHARENKO \n"
        "📞 Phone Number: 386-225-1619 \n"
        "🚛 Truck Number: 19 \n"
        "🚂 Trailer Number: 19 \n"
        "🔑 VIN:3C63RRGL2RG219808 \n" 
        "⚓Ramps: 14ft \n"
        "⚖ Weight: 8200lb \n"
        "🅱 Owner: Ruslan ",
    ),
    "Водитель DARMAN ORUZBAEV": (
        "📌 Driver Name: DARMAN ORUZBAEV \n"
        "📞 Phone Number: 718-344-0617 \n"
        "🚛 Truck Number: 4 \n"
        "🚂 Trailer Number: 4 \n"
        "🔑 VIN:3C63RRHLXRG341413 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex ",
    ),
    "Водитель TOTRAZ ABAEV": (
        "📌 Driver Name: TOTRAZ ABAEV \n"
        "📞 Phone Number: 754-286-7577 \n"
        "🚛 Truck Number: 16 \n"
        "🚂 Trailer Number: 16 \n"
        "🔑 VIN:3C63RRHL2PG643033 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas ",
    ),
    "Водитель YERKEBULAN BOSHAIBEKOV": (
        "📌 Driver Name: YERKEBULAN BOSHAIBEKOV \n"
        "📞 Phone Number: 773-751-9292 \n"
        "🚛 Truck Number: 18 \n"
        "🚂 Trailer Number: 18 \n"
        "🔑 VIN:3C63RRHL0RG289662 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8100lb \n"
        "🅱 Owner: Dumitru OU ",
    ),
    "Водитель MAIRBEK KHASIGOV": (
        "📌 Driver Name: MAIRBEK KHASIGOV \n"
        "📞 Phone Number: 925-497-0899 \n"
        "🚛 Truck Number: 32 \n"
        "🚂 Trailer Number: 32 \n"
        "🔑 VIN:3C63RRHL2RG289436 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Stas ",
    ),
    "Водитель MARIN GULIA": (
        "📌 Driver Name: MARIN GULIA \n"
        "📞 Phone Number: 916-912-7398 \n"
        "🚛 Truck Number: 26 \n"
        "🚂 Trailer Number: 26 \n"
        "🔑 VIN:1GT49LEY8RF467913 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 9500lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель ALBERT ABAIKHANOV": (
        "📌 Driver Name: ALBERT ABAIKHANOV \n"
        "📞 Phone Number: 347-739-8531 \n"
        "🚛 Truck Number: 22 \n"
        "🚂 Trailer Number: 22 \n"
        "🔑 VIN:3C63RRHL9KG642308 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8860lb \n"
        "🅱 Owner: Rassul ",
    ),
    "Водитель ASKHABALI SHABANOV": (
        "📌 Driver Name: ASKHABALI SHABANOV \n"
        "📞 Phone Number: 520-994-9999 \n"
        "🚛 Truck Number: 7 \n"
        "🚂 Trailer Number: 7 \n"
        "🔑 VIN:3C63RRHL4RG358188 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9360lb \n"
        "🅱 Owner: Alex ",
    ),
    "Водитель ILLIA HORBATOK": (
        "📌 Driver Name: ILLIA HORBATOK \n"
        "📞 Phone Number: 701-403-0994 \n"
        "🚛 Truck Number: 2 \n"
        "🚂 Trailer Number: 2 \n"
        "🔑 VIN:3C63RRHL2RG358187 \n"
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8720lb \n"
        "🅱 Owner: Alex ",
    ),
    "Водитель TSYDEN TOBODORZHIEV": (
        "📌 Driver Name: TSYDEN TOBODORZHIEV \n"
        "📞 Phone Number: 347-232-8827 \n"
        "🚛 Truck Number: 36 \n"
        "🚂 Trailer Number: 36 \n"
        "🔑 VIN:1FT8W3DT3REF83199 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator",
    ),
    "Водитель VIKTOR ATANOV": (
        "📌 Driver Name: VIKTOR ATANOV \n"
        "📞 Phone Number: 929-481-9521 \n"
        "🚛 Truck Number: 39 \n"
        "🚂 Trailer Number: 39 \n"
        "🔑 VIN:1FT8W3DT9REE49099 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 10000lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель AZAT AZAMAT": (
        "📌 Driver Name: AZAT AZAMAT \n"
        "📞 Phone Number: 253-286-8080 \n"
        "🚛 Truck Number: 29 \n"
        "🚂 Trailer Number: 29 \n"
        "🔑 VIN:3C63RRGL6RG382381 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 8680lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель GEORGII RIONELI": (
        "📌 Driver Name: GEORGII RIONELI \n"
        "📞 Phone Number: 925-440-1503 \n"
        "🚛 Truck Number: 35 \n"
        "🚂 Trailer Number: 35 \n"
        "🔑 VIN:3C63RRGL0NG356465 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель DENIS COLESNICENCO": (
        "📌 Driver Name: DENIS COLESNICENC \n"
        "📞 Phone Number: 630-352-9196 \n"
        "🚛 Truck Number: 38 \n"
        "🚂 Trailer Number: 38 \n"
        "🔑 VIN:3C63RRHL6RG289522 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9600lb \n"
        "🅱 Owner: Gheorghe Balica ",
    ),
    "Водитель IGOR BALAKIN": (
        "📌 Driver Name: IGOR BALAKIN \n"
        "📞 Phone Number: 331-229-8750 \n"
        "🚛 Truck Number: 20 \n"
        "🚂 Trailer Number: 20 \n"
        "🔑 VIN:3C63RRGL3KG618197 \n" 
        "⚓Ramps: Mega Ramps \n"
        "⚖ Weight: 8700lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель TAULAN TOTORKULOV": (
        "📌 Driver Name: TAULAN TOTORKULOV \n"
        "📞 Phone Number: 224-463-0235 \n"
        "🚛 Truck Number: 5 \n"
        "🚂 Trailer Number: 5 \n"
        "🔑 VIN:3C63RRGL9KG700614 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9700lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель ERDEM DORZHIEV": (
        "📌 Driver Name: ERDEM DORZHIEV \n"
        "📞 Phone Number: 412-304-4565 \n"
        "🚛 Truck Number: 8 \n"
        "🚂 Trailer Number: 8 \n"
        "🔑 VIN:3C63R3GL6NG159989 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator ",
    ),
    "Водитель (Said) MAGOMEDSAID GABIBULAEV": (
        "📌 Driver Name: MAGOMEDSAID GABIBULAEV \n"
        "📞 Phone Number: 305-391-1839 \n"
        "🚛 Truck Number: 6 \n"
        "🚂 Trailer Number: 6 \n"
        "🔑 VIN:3C63RRGL0RG183858 \n" 
        "⚓Ramps: 12ft \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Ruslan ",
    ),
    "Водитель (DOS) DASTAN MASYLKANOV": (
        "📌 Driver Name: DASTAN MASYLKANOV \n"
        "📞 Phone Number: 917-704-3848 \n"
        "🚛 Truck Number: 37 \n"
        "🚂 Trailer Number: 37 \n"
        "🔑 VIN:3C63RRHL6RG307632 \n" 
        "⚓Ramps: n/a \n"
        "⚖ Weight: 8500lb \n"
        "🅱 Owner: Alex ",
    ),
    "Водитель SOSLAN GAGLOEV": (
        "📌 Driver Name: SOSLAN GAGLOEV \n"
        "📞 Phone Number: 786-868-5690 \n"
        "🚛 Truck Number: 13 \n"
        "🚂 Trailer Number: 13 \n"
        "🔑 VIN:3C63RRGL7RG295329 \n" 
        "⚓Ramps: 8ft \n"
        "⚖ Weight: 9000lb \n"
        "🅱 Owner: Owner Operator ",
    ),
}

# Функция для отображения списка диспетчеров
async def show_dispatchers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in dispatchers.keys()]
    keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='start')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.edit_text("👥 Выберите диспетчера:", reply_markup=reply_markup)

# Функция для отображения списка водителей диспетчера
async def show_drivers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    dispatcher_name = query.data
    if dispatcher_name in dispatchers:
        drivers = dispatchers[dispatcher_name]
        keyboard = [[InlineKeyboardButton(driver, callback_data=driver)] for driver in drivers]
        keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data='dispatchers')])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(f"🚛 Список водителей {dispatcher_name}:", reply_markup=reply_markup)

# Информация о водителе с кнопкой для загрузки файла
async def show_driver_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    driver_name = query.data
    if driver_name == "Водитель Erdem":
        # Добавляем кнопку для отправки файла
        keyboard = [
            [InlineKeyboardButton("📂 Скачать файл", callback_data="send_file_erdem")],
            [InlineKeyboardButton("⬅️ Назад", callback_data='drivers')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("📌 Информация о водителе Erdem", reply_markup=reply_markup)

# Обработчик для кнопки с отправкой файла
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    driver_name = query.data

    if driver_name == "send_file_erdem":
        document_path = "https://drive.google.com/uc?id=18xK7GtULLpYmROzjKRlxXVTVamsfrPlj"  # Прямая ссылка на файл
        # Отправляем файл в чат
        await query.message.reply_document(document=document_path, caption="📂 Файл для водителя Erdem")

# Основной обработчик
async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_access(update):
        return

    # Слушаем команды
    if update.message:
        text = update.message.text.lower()
        if text == "/start":
            await start(update, context)
        else:
            await button_handler(update, context)
    elif update.callback_query:
        query = update.callback_query
        if query.data == 'dispatchers':
            await show_dispatchers(update, context)
        elif query.data in dispatchers:
            await show_drivers(update, context)
        elif query.data in drivers_info:
            await show_driver_info(update, context)

if __name__ == "__main__":
    application = Application.builder().token('8109632757:AAHJDDDcfidBLLym_ZDYIu4bH001P1LkcKE').build()

    # Регистрация команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(main))

    # Запуск бота
    application.run_polling()
