from aiogram import types  # Импортируем классы из библиотеки aiogram для работы с Telegram Bot API

# Создаем кнопки для клавиатуры
button1 = types.KeyboardButton(text='/start')  # Кнопка "/start" для начала взаимодействия с ботом
button2 = types.KeyboardButton(text='/stop')   # Кнопка "/stop" для остановки какого-то процесса или функции
button3 = types.KeyboardButton(text='Инфо')    # Кнопка "Инфо" для получения информации о боте или его функциях

# Создаем массив из двух строк с кнопками
# Каждый внутренний список представляет собой строку клавиатуры, а элементы списка — кнопки, расположенные в этой строке
keyboard1 = [
    [button1, button2, button3],  # Первая строка клавиатуры с кнопками "/start", "/stop" и "Инфо"
    [button3, button1, button2]   # Вторая строка клавиатуры с кнопками "Инфо", "/start" и "/stop"
]

# Создаем объект клавиатуры с указанными кнопками
# Используем ReplyKeyboardMarkup для создания клавиатуры, которая будет отображаться в ответах бота
# Параметр resize_keyboard=True указывает, что клавиатура должна быть адаптирована под размер экрана устройства пользователя
keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
