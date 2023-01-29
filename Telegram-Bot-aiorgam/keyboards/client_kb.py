from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/режим')
b2 = KeyboardButton('/адрес')
b3 = KeyboardButton('/меню')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить где я', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).insert(b3).row(b4, b5)

#kb_client.row(b1, b2, b3)

