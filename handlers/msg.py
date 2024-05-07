from aiogram import Router, types, F

# Создаем объект Router для обработки маршрутов
router = Router()

# Определяем обработчик сообщений для любого текстового сообщения
@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    else:
        await message.reply('Не понимаю тебя...')
