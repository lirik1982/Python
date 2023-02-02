from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from date_base import sql_lite

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Поехали!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом lirik1982, напишите ему:\nhttps://t.me/lirik1982_bot')

#@dp.message_handler(commands=['Режим'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, '24\\7!')

#@dp.message_handler(commands=['Адрес'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Запорная, 44', reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['меню'])
async def pizza_menu_command(message: types.Message):
    await sql_lite.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['режим'])
    dp.register_message_handler(pizza_place_command, commands=['адрес'])
    dp.register_message_handler(pizza_menu_command, commands=['меню'])
