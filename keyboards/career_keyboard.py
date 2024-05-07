from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from typing import List

def make_keyboard(items: List[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    keyboard = ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    return keyboard
