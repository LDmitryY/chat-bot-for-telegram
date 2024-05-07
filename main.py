import asyncio
import config  # Импортируем модуль config для доступа к настройкам бота
from aiogram import Bot, Dispatcher  # Импортируем классы Bot и Dispatcher из библиотеки aiogram для работы с Telegram API
import logging  # Импортируем модуль logging для настройки вывода логов
from handlers import common, msg, career_choice  # Импортируем обработчики сообщений из модуля handlers

# Определяем асинхронную функцию main, которая будет запускать бота
async def main():
    # Настраиваем уровень логирования на INFO
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота с использованием токена из модуля config
    bot = Bot(token=config.token)
    # Создаем диспетчер для обработки входящих сообщений
    dp = Dispatcher()

    # Регистрируем обработчики сообщений в диспетчере
    dp.include_router(common.router)  # Общие обработчики
    dp.include_router(career_choice.router)  # Обработчики выбора карьеры
    dp.include_router(msg.router)  # Обработчики простых сообщений

    # Запускаем бота на опрос сообщений
    await dp.start_polling(bot)

# Проверяем, что код запускается напрямую (а не импортируется как модуль)
if __name__ == '__main__':
    # Запускаем основную асинхронную функцию main
    asyncio.run(main())
