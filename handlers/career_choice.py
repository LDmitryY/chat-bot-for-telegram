from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.career_keyboard import make_keyboard

# Создаем объект Router для обработки маршрутов
router = Router()

# Определяем доступные профессии и оценки
available_jobs = [
    'Программист',
    'Маркетолог',
    'Менеджер',
    'Аналитик',
    'Бухгалтер'
]
available_grades = [
    'Низкий',
    'Средний',
    'Высокий'
]

# Определяем состояния для выбора профессии и оценки
class Choice(StatesGroup):
    job = State()
    grade = State()

# Обработчик команды /prof
@router.message(Command(commands=['prof']))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Какая профессия вас интересует?', reply_markup=make_keyboard(available_jobs))
    await state.set_state(Choice.job)

# Обработчик выбора профессии
@router.message(Choice.job, F.text.in_(available_jobs))
async def jobs(message: types.Message, state: FSMContext):
    await message.answer('Как вы оцениваете свою профессию?', reply_markup=make_keyboard(available_grades))
    await state.set_state(Choice.grade)

# Обработчик неправильного выбора профессии
@router.message(Choice.job)
async def job_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_jobs))

# Обработчик выбора оценки
@router.message(Choice.grade, F.text.in_(available_grades))
async def grade(message: types.Message, state: FSMContext):
    await message.answer(f'Вы всё прошли, с вами свяжутся наши hr {message.text}',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

# Обработчик неправильного выбора оценки
@router.message(Choice.grade)
async def grade_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_grades))
