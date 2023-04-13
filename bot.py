import asyncio

from config import TOKEN
import keyboards as kbs
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import InputFile, callback_query, message, CallbackQuery
import logging
import sqlite3
from aiogram.types import Message
from study import main_workers_command, structure_command, instr_question1_handler, instr_question2_handler, \
    instr_question3_handler, \
    instr_question4_handler, tasks_question1_handler, tasks_question2_handler, tasks_question3_handler, \
    sec_question1_handler, sec_question2_handler, sec_question3_handler

# подключение к базе данных
con = sqlite3.connect(r'tb.db')
cur = con.cursor()

conn1 = sqlite3.connect(r"admin.db")
cur1 = conn1.cursor()

cur1.execute("""CREATE TABLE IF NOT EXISTS question(
id INTEGER NOT NULL PRIMARY KEY,
user_text TEXT,
answer TEXT);
""")

conn1.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Fio(
id INTEGER NOT NULL PRIMARY KEY,
Имя TEXT,
Фамилия TEXT,
Специальность TEXT,
username TEXT,
progress INTEGER,
user_id INTEGER);
""")

# логирование
logging.basicConfig(level=logging.INFO)

# бот и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# счетчик прогресса
async def progress_count(user_id):
    query = f"UPDATE Fio SET progress = progress + 1 WHERE user_id = ?"
    cur.execute(query, (user_id,))
    con.commit()


# добавление в базу данных
def idd(Name, Sur_Name, spes, username, progress, user_id):
    last_id = cur.execute('SELECT MAX (id) FROM Fio').fetchone()

    if last_id[0] is None:
        id = 1
    else:
        id = last_id[0] + 1

    cur.execute(
        'INSERT INTO Fio VALUES ({},"{}", "{}", "{}", "{}", "{}", "{}")'.format(id, Name, Sur_Name, spes, username, progress, user_id))
    con.commit()

    cur.execute("SELECT * FROM Fio;")
    one_result = cur.fetchall()
    for i in one_result:
        print(i)


progress = 0


# старт
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой новый чат-бот для онбординга "
                         "в нашей компании! Меня создали, "
                         "чтобы помочь тебе присоединиться к нашей "
                         "команде с минимальным стрессом и максимальным "
                         "комфортом. Я помогу тебе ознакомиться с нашей "
                         "компанией и подготовиться к работе здесь. Давай начнем!",
                         reply_markup=kbs.registration_keyboard)


# обработка регистрации
@dp.callback_query_handler(lambda c: c.data == 'reg_but')
async def register_command(message: types.Message):
    # здесь получаем данные
    await bot.send_message(message.from_user.id, 'Введите имя, фамилию, специальность :')

    @dp.message_handler()
    async def name(message: types.Message):
        words = message.text
        words = words.split()
        await bot.send_message(message.from_user.id, f"Вы зарегистрированы!", reply_markup=kbs.menu_button)
        idd(words[0], words[1], words[2], message.from_user.username, progress, message.from_user.id)


# обработка меню
@dp.message_handler(text='Меню')
async def process_menu_message(message: types.Message):
    if message.text.lower() == 'меню':
        await bot.send_message(message.chat.id, 'Меню:', reply_markup=kbs.menu_keyboard)


# обработка кнопки обучения
@dp.callback_query_handler(lambda a: a.data == 'study_but')
async def study_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Обучение навыкам', reply_markup=kbs.study_keyboard)


# обработка кнопки офис
@dp.callback_query_handler(lambda b: b.data == 'office_but')
async def study_command(callback_query: types.CallbackQuery):
    office_photo1 = InputFile("media/office1.jpg")
    office_photo2 = InputFile("media/office2.jpg")
    office_photo3 = InputFile("media/office3.jpg")

    await bot.send_message(callback_query.from_user.id, 'Наш офис: ')
    await bot.send_photo(callback_query.from_user.id, office_photo1)
    await bot.send_photo(callback_query.from_user.id, office_photo2)
    await bot.send_photo(callback_query.from_user.id, office_photo3)



# обработка кнопки сотрудники
@dp.callback_query_handler(lambda f: f.data == 'workers_but')
async def workers_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Наши сотрудники:')
    cur.execute("SELECT * FROM Fio;")
    one_result = cur.fetchall()
    for i in one_result:
        try:
            photos = await bot.get_user_profile_photos(i[6], limit=10)
            photo_file = photos.photos[0][-1].file_id
            await bot.send_photo(callback_query.from_user.id, photo_file, f"{i[1]} {i[2]}\n"
                                                                           f"{i[3]}\n"
                                                                           f"@{i[4]}")
        except Exception as e:
            print(e)
            await bot.send_message(callback_query.from_user.id, "Не удалось получить фото профиля\n"
                                                                f"{i[1]} {i[2]}\n"
                                                                f"{i[3]}\n"
                                                                f"@{i[4]}")



# обработка кнопки информация о компании
@dp.callback_query_handler(lambda y: y.data == 'info_but')
async def info_command(callback_query: types.CallbackQuery):
    logo = InputFile("media/logo.png")
    await bot.send_photo(callback_query.from_user.id, logo, 'Мы создаем инновационные решения, '
                                                            'основанные на передовых технологиях, чтобы помочь '
                                                            'нашим клиентам эффективно управлять и развивать свой '
                                                            'бизнес. Мы предоставляем полный спектр услуг, от '
                                                            'разработки программного обеспечения до консультирования '
                                                            'по внедрению технологических решений, а также обеспечиваем '
                                                            'техническую поддержку и обслуживание.')
    await bot.send_message(callback_query.from_user.id,
                           'Мы ценим индивидуальный подход к каждому клиенту и работаем над '
                           'тем, чтобы наши решения были максимально адаптированы к их '
                           'уникальным потребностям и целям. Наша команда состоит из '
                           'опытных разработчиков и консультантов, готовых предложить '
                           'лучшие практики и решения в области информационных технологий. '
                           'Мы стремимся быть надежным партнером для наших клиентов и '
                           'вместе с ними расти и развиваться в технологически быстро '
                           'меняющемся мире.')


# обработка кнопки профиль
@dp.callback_query_handler(lambda n: n.data == 'profile_but')
async def profile_command(message: types.Message):
    query = f"SELECT Имя FROM Fio WHERE username = ?"
    cur.execute(query, (message.from_user.username,))
    results = cur.fetchone()[0]

    query1 = f"SELECT Фамилия FROM Fio WHERE username = ?"
    cur.execute(query1, (message.from_user.username,))
    results1 = cur.fetchone()[0]

    query2 = f"SELECT Специальность FROM Fio WHERE username = ?"
    cur.execute(query2, (message.from_user.username,))
    results2 = cur.fetchone()[0]

    query3 = f"SELECT Progress FROM Fio WHERE username = ?"
    cur.execute(query3, (message.from_user.username,))
    results3 = cur.fetchone()[0]

    photo_query = f"SELECT user_id FROM Fio WHERE username = ?"
    cur.execute(photo_query, (message.from_user.username,))
    photo_query_result = cur.fetchone()[0]

    study_string = ""
    if results3 >= 5:
        study_string = "пройдено"
    elif results3 < 5:
        study_string = f"{results3} из 5"

    try:
        photos = await bot.get_user_profile_photos(photo_query_result, limit=10)
        photo_file = photos.photos[0][-1].file_id
        await bot.send_photo(message.from_user.id, photo_file, f'Ваш профиль:\n'
                                                               f'Имя: {results}\n'
                                                               f'Фамилия: {results1}\n'
                                                               f'Специальность: {results2}\n'
                                                               f'Обучение: {study_string}')
    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, f'У вас нет аватарки\n'
                                                     f'Ваш профиль:\n'
                                                     f'Имя: {results}\n'
                                                     f'Фамилия: {results1}\n'
                                                     f'Специальность: {results2}\n'
                                                     f'Обучение: {study_string}')


# обработка ключевых сотрудников
@dp.callback_query_handler(lambda p: p.data == 'main_workers_but')
async def mworkers_command(callback_query: types.CallbackQuery):
    await progress_count(callback_query.from_user.id)
    await main_workers_command(callback_query)


user_score = 0


# обработка структуры
@dp.callback_query_handler(lambda z: z.data == 'struct_but')
async def struct_command(callback_query: types.CallbackQuery):
    await structure_command(callback_query)
    await progress_count(callback_query.from_user.id)


# Описываем обработчик нажатий на кнопки
dp.callback_query_handler(instr_question1_handler, kbs.question1_cb.filter())
dp.callback_query_handler(instr_question2_handler, kbs.question2_cb.filter())
dp.callback_query_handler(instr_question3_handler, kbs.question3_cb.filter())
dp.callback_query_handler(instr_question4_handler, kbs.question4_cb.filter())

dp.callback_query_handler(tasks_question1_handler, kbs.question1_cb.filter())
dp.callback_query_handler(tasks_question2_handler, kbs.question2_cb.filter())
dp.callback_query_handler(tasks_question3_handler, kbs.question3_cb.filter())

dp.callback_query_handler(sec_question1_handler, kbs.sec_question1_cb.filter())
dp.callback_query_handler(sec_question2_handler, kbs.sec_question2_cb.filter())
dp.callback_query_handler(sec_question3_handler, kbs.sec_question3_cb.filter())


# обработка инструментов
@dp.callback_query_handler(lambda x: x.data == 'instr_but')
async def instr_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Ответьте на вопросы теста:')
    # Отправляем первый вопрос
    await bot.send_message(callback_query.from_user.id, 'Какой инструмент используется для веб-разработки на Python?',
                           reply_markup=kbs.question1_buttons)


# Описываем обработчик нажатий на кнопки
@dp.callback_query_handler(kbs.question1_cb.filter())
async def question1_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'b':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    # Отправляем второй вопрос
    await callback_query.message.answer(
        'Какой язык программирования используется для написания приложений для Android?',
        reply_markup=kbs.question2_buttons)


@dp.callback_query_handler(kbs.question2_cb.filter())
async def question2_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'a':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    # Отправляем третий вопрос
    await callback_query.message.answer('Какой фреймворк используется для разработки веб-приложений на Java?',
                                        reply_markup=kbs.question3_buttons)


@dp.callback_query_handler(kbs.question3_cb.filter())
async def question3_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'b':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    # Отправляем четвертый вопрос
    await callback_query.message.answer('Какой инструмент используется для создания приложений на платформе Windows?',
                                        reply_markup=kbs.question4_buttons)


@dp.callback_query_handler(kbs.question4_cb.filter())
async def question4_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'b':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    # Завершаем тест
    await callback_query.message.answer('Тест окончен. Спасибо за участие!')
    await progress_count(callback_query.from_user.id)


# обработка задач
@dp.callback_query_handler(lambda t: t.data == 'tasks_but')
async def tasks_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Ответьте на вопросы теста:')
    # Отправляем первый вопрос
    await bot.send_message(callback_query.from_user.id, 'Какую из перечисленных услуг предоставляет наша компания?',
                           reply_markup=kbs.tasks_question1_buttons)


@dp.callback_query_handler(kbs.tsk_question1_cb.filter())
async def tasks_question1_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'b':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    await callback_query.message.answer('Что входит в услуги компании?', reply_markup=kbs.tasks_question2_buttons)


@dp.callback_query_handler(kbs.tsk_question2_cb.filter())
async def tasks_question2_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'b':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    await callback_query.message.answer('Какую из перечисленных проблему решает компания?',
                                        reply_markup=kbs.tasks_question3_buttons)


@dp.callback_query_handler(kbs.tsk_question3_cb.filter())
async def tasks_question3_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'b':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    await callback_query.message.answer('Тест окончен. Спасибо за участие!')
    await progress_count(callback_query.from_user.id)


@dp.callback_query_handler(lambda g: g.data == 'secur_but')
async def sec_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Ответьте на вопросы теста:')
    # Отправляем первый вопрос
    await bot.send_message(callback_query.from_user.id, 'Какой тип атаки может быть вызван путем отправки '
                                                        'поддельного электронного письма от имени доверенного '
                                                        'отправителя, чтобы получить конфиденциальную информацию '
                                                        'от сотрудника компании?',
                           reply_markup=kbs.sec_question1_buttons)


@dp.callback_query_handler(kbs.sec_question1_cb.filter())
async def sec_question1_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'a':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    await callback_query.message.answer('Какой вид защиты может обеспечить компания для '
                                        'защиты своей сети и компьютеров от вредоносного '
                                        'программного обеспечения?', reply_markup=kbs.sec_question2_buttons)


@dp.callback_query_handler(kbs.sec_question2_cb.filter())
async def sec_question2_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'a':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    await callback_query.message.answer('Что следует делать, если вы получаете электронное письмо '
                                        'от неизвестного отправителя с подозрительной '
                                        'ссылкой или вложением?', reply_markup=kbs.sec_question3_buttons)


@dp.callback_query_handler(kbs.sec_question3_cb.filter())
async def sec_question3_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    while answer != 'b':
        await callback_query.answer('Неправильно.')
    await callback_query.answer('Правильно!')
    await callback_query.message.answer('Тест окончен. Спасибо за участие!')
    await progress_count(callback_query.from_user.id)


# поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
