from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Создание клавиатуры регистрации
from aiogram.utils.callback_data import CallbackData

registration_keyboard = InlineKeyboardMarkup()
reg_button = InlineKeyboardButton('Зарегистрироваться', callback_data='reg_but')

registration_keyboard.add(reg_button)


# создание клавиатуры меню
menu_keyboard = InlineKeyboardMarkup()
study_button = InlineKeyboardButton('Обучение', callback_data='study_but')
office_button = InlineKeyboardButton('Офис', callback_data='office_but')
workers_button = InlineKeyboardButton('Сотрудники', callback_data='workers_but')
profile_button = InlineKeyboardButton('Профиль', callback_data='profile_but')
info_button = InlineKeyboardButton('Информация о компании', callback_data='info_but')

menu_keyboard.row(study_button, office_button)
menu_keyboard.row(workers_button, profile_button)
menu_keyboard.add(info_button)


# создание клавиатуры специальностей
specialties_keyboard = InlineKeyboardMarkup()
frontend_button = InlineKeyboardButton('Фронтенд-разработчик', callback_data='front_but')
backend_button = InlineKeyboardButton('Бэкенд-разработчик', callback_data='backend_but')
tester_button = InlineKeyboardButton('Тестировщик', callback_data='tester_but')

specialties_keyboard.add(frontend_button)
specialties_keyboard.add(backend_button)
specialties_keyboard.add(tester_button)


# создание клавиатуры обучения
study_keyboard = InlineKeyboardMarkup()
main_workers_button = InlineKeyboardButton('Ключевые сотрудники', callback_data='main_workers_but')
structures_button = InlineKeyboardButton('Структура компании', callback_data='struct_but')
instruments_button = InlineKeyboardButton('Инструменты', callback_data='instr_but')
tasks_button = InlineKeyboardButton('Задачи', callback_data='tasks_but')
security_button = InlineKeyboardButton('Безопасность', callback_data='secur_but')

study_keyboard.add(main_workers_button)
study_keyboard.add(structures_button)
study_keyboard.row(instruments_button, tasks_button)
study_keyboard.add(security_button)


# создание клавиатуры сотрудников
workers_keyboard = InlineKeyboardMarkup()
developer_department_button = InlineKeyboardButton('Отдел разработки', callback_data='dev_dep_but')
testing_department_button = InlineKeyboardButton('Отдел тестирования', callback_data='test_dep_but')

workers_keyboard.row(developer_department_button, testing_department_button)


# Создание кнопки меню
button = KeyboardButton('Меню')

menu_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button)


# клавиатура для теста
# Создаем CallbackData-объект для каждого вопроса
question1_cb = CallbackData('question1', 'answer')
question2_cb = CallbackData('question2', 'answer')
question3_cb = CallbackData('question3', 'answer')
question4_cb = CallbackData('question4', 'answer')

# Создаем кнопки с вариантами ответов для каждого вопроса для инструментов
question1_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Ruby on Rails', callback_data=question1_cb.new(answer='a')),
    InlineKeyboardButton('Django', callback_data=question1_cb.new(answer='b')),
    InlineKeyboardButton('ReactJS', callback_data=question1_cb.new(answer='c'))
)
question2_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Java', callback_data=question2_cb.new(answer='a')),
    InlineKeyboardButton('Python', callback_data=question2_cb.new(answer='b')),
    InlineKeyboardButton('Ruby', callback_data=question2_cb.new(answer='c'))
)
question3_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('.NET', callback_data=question3_cb.new(answer='a')),
    InlineKeyboardButton('Spring', callback_data=question3_cb.new(answer='b')),
    InlineKeyboardButton('Flask', callback_data=question3_cb.new(answer='c'))
)
question4_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Python', callback_data=question4_cb.new(answer='a')),
    InlineKeyboardButton('C#', callback_data=question4_cb.new(answer='b')),
    InlineKeyboardButton('PHP', callback_data=question4_cb.new(answer='c'))
)


tsk_question1_cb = CallbackData('tsk_question1', 'answer')
tsk_question2_cb = CallbackData('tsk_question2', 'answer')
tsk_question3_cb = CallbackData('tsk_question3', 'answer')
tsk_question4_cb = CallbackData('tsk_question4', 'answer')

# кнопки для теста на знание задач
tasks_question1_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Производство телефонов', callback_data=tsk_question1_cb.new(answer='a')),
    InlineKeyboardButton('Разработка веб-приложений', callback_data=tsk_question1_cb.new(answer='b')),
    InlineKeyboardButton('Организация праздников', callback_data=tsk_question1_cb.new(answer='c'))
)
tasks_question2_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Доставка пиццы', callback_data=tsk_question2_cb.new(answer='a')),
    InlineKeyboardButton('Разработка десктопных программ', callback_data=tsk_question2_cb.new(answer='b')),
    InlineKeyboardButton('Проведение медицинских исследований', callback_data=tsk_question2_cb.new(answer='c'))
)
tasks_question3_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Увеличение заболеваемости гриппом', callback_data=tsk_question3_cb.new(answer='a')),
    InlineKeyboardButton('Консультации по внедрению технологических решений', callback_data=tsk_question3_cb.new(answer='b')),
    InlineKeyboardButton('Ремонт автомобилей', callback_data=tsk_question3_cb.new(answer='c'))
)


sec_question1_cb = CallbackData('sec_question1', 'answer')
sec_question2_cb = CallbackData('sec_question2', 'answer')
sec_question3_cb = CallbackData('sec_question3', 'answer')

# кнопки для теста на знание безопасности
sec_question1_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Фишинг', callback_data=sec_question1_cb.new(answer='a')),
    InlineKeyboardButton('Малвертайзинг', callback_data=sec_question1_cb.new(answer='b')),
    InlineKeyboardButton('ДДоС-атака', callback_data=sec_question1_cb.new(answer='c'))
)
sec_question2_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Установка антивирусного ПО', callback_data=sec_question2_cb.new(answer='a')),
    InlineKeyboardButton('Ежедневная молитва от вирусов', callback_data=sec_question2_cb.new(answer='b')),
    InlineKeyboardButton('Запрет на использование Wi-Fi в офисе', callback_data=sec_question2_cb.new(answer='c'))
)
sec_question3_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Немедленно кликнуть на ссылку, чтобы узнать, что находится по ссылке', callback_data=sec_question3_cb.new(answer='a')),
    InlineKeyboardButton('Сразу же удалить письмо', callback_data=sec_question3_cb.new(answer='b')),
    InlineKeyboardButton('Отправить письмо своему начальнику и спросить, что делать', callback_data=sec_question3_cb.new(answer='c'))
)
