from aiogram import Bot, Dispatcher, types, executor
import sqlite3
from config import TOKEN
from aiogram.types import Message, InputFile, message, CallbackQuery
import random
import keyboards as kbs

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def main_workers_command(callback_query: types.CallbackQuery):
    developer_photo1 = InputFile("media/dev1.jpg")
    developer_photo2 = InputFile("media/dev2.jpg")
    await bot.send_photo(callback_query.from_user.id, developer_photo1, 'Максим Каничев\nБэкенд-разработчик')
    await bot.send_photo(callback_query.from_user.id, developer_photo2, 'Георгий Беришвили\nБэкенд-разработчик')


async def structure_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Структура нашей компании: ')
    await bot.send_message(callback_query.from_user.id, 'Руководитель - отвечает за общее управление '
                                                        'компанией и принимает стратегические решения.')
    await bot.send_message(callback_query.from_user.id, 'Разработчики - отвечают за создание '
                                                        'программного обеспечения и техническую поддержку.')
    await bot.send_message(callback_query.from_user.id, 'Менеджер по продажам - отвечает за продажи '
                                                        'продуктов и услуг компании.')
    await bot.send_message(callback_query.from_user.id, 'Тестировщик - отвечает за тестирование '
                                                        'продуктов компании, выявление ошибок '
                                                        'в коде и сообщает об этом разработчикам.')


# Описываем обработчики нажатий на кнопки
async def instr_question1_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')

async def instr_question2_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'a':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')

async def instr_question3_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')

async def instr_question4_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')



async def tasks_question1_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')

async def tasks_question2_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')

async def tasks_question3_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')


async def sec_question1_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')

async def sec_question2_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')

async def sec_question3_handler(callback_query: CallbackQuery, callback_data: dict):
    answer = callback_data['answer']
    if answer == 'b':
        await callback_query.answer('Правильно!')
    else:
        await callback_query.answer('Неправильно.')