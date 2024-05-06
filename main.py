import asyncio  # Импортируем модуль asyncio для работы с асинхронным кодом
import config  # Импортируем модуль config для получения токена бота
from aiogram import Bot, Dispatcher, types, F  # Импортируем необходимые классы из библиотеки aiogram
from aiogram.filters.command import Command  # Импортируем класс Command для обработки команд
import logging  # Импортируем модуль logging для настройки логирования
import random  # Импортируем модуль random для генерации случайных чисел
from keyboards import keyboard  # Импортируем пользовательскую клавиатуру из модуля keyboards

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота и диспетчера
bot = Bot(token=config.token)  # Создаем объект бота, используя токен из модуля config
dp = Dispatcher()  # Создаем объект диспетчера для обработки входящих сообщений

# Обработчик команды /start
@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! Я чатбот для общения, меня создал Дмитрий! Чтобы проверить мою работу напиши или выбери команты в чате.', reply_markup=keyboard)

# Обработчик команды /стоп и /stop
@dp.message(Command(commands=['стоп']))
@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    print(message.from_user.full_name)  # Выводим имя пользователя в консоль
    await message.answer(f'Пока, {message.chat.first_name}!')

# Обработчик команды /инфо и /info, а также текста "инфо"
@dp.message(Command(commands=['инфо', 'info']))
@dp.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(0, 100)  # Генерируем случайное число от 0 до 100
    await message.answer(f'Привет, твоё число: {number}!')

# Обработчик всех текстовых сообщений
@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():  # Если сообщение содержит "привет"
        await message.reply('И тебе привет!')  # Отвечаем пользователю приветствием
    elif 'как дела' in message.text.lower():  # Если сообщение содержит "как дела"
        await message.reply('Нормально, а у тебя?')  # Спрашиваем у пользователя как у него дела
    else:
        await message.reply('Не понимаю тебя...')  # Если не распознано, отвечаем стандартным сообщением

# Асинхронная функция для запуска бота
async def main():
    await dp.start_polling(bot)  # Запускаем бота для получения обновлений

# Проверяем, что код запускается напрямую, а не импортируется в другой модуль
if __name__ == '__main__':
    asyncio.run(main())  # Запускаем асинхронную функцию main()
