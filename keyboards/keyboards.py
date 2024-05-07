from aiogram import types

# Создаем объекты KeyboardButton для каждой кнопки
button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='Инфо')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='/prof')

# Создаем список списков кнопок для формирования клавиатуры
keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button2]
]

# Создаем объект ReplyKeyboardMarkup с заданными кнопками и включаем опцию изменения размера клавиатуры
keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
