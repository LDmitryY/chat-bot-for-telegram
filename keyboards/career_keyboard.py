from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from typing import List

def make_keyboard(items: List[str]) -> ReplyKeyboardMarkup:
    # Создаем список кнопок, преобразуя каждый элемент списка в объект KeyboardButton
    row = [KeyboardButton(text=item) for item in items]
    
    # Создаем объект ReplyKeyboardMarkup с рядом кнопок и включаем опцию изменения размера клавиатуры
    keyboard = ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    
    # Возвращаем созданную клавиатуру
    return keyboard
