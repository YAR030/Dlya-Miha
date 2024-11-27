from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

button_perevod = InlineKeyboardButton(text="Посчитать стоимость", callback_data="perevod")
button_questions = InlineKeyboardButton(text="Вопрорсы", callback_data="questions")
button_manager = InlineKeyboardButton(text="Связаться c менеджером", url="https://t.me/minn0nn")

main_keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[[button_perevod], [button_questions], [button_manager]])


b_to_menu = InlineKeyboardButton(text="Назад", callback_data="menu")
b_to_q = InlineKeyboardButton(text="Назад", callback_data="questions")
b_to_dostavka = InlineKeyboardButton(text="📦Доставка📦", callback_data="dostavka")

inline_to_dostavka_keyboard = InlineKeyboardMarkup(inline_keyboard=[[b_to_dostavka], [b_to_menu]])
inline_to_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[[b_to_menu]])
inline_to_q_keyboard = InlineKeyboardMarkup(inline_keyboard=[[b_to_q]])

b_q1 = InlineKeyboardButton(text="Что такое Poizon?", callback_data="q1")
b_q2 = InlineKeyboardButton(text="Какие сроки доставки?", callback_data="q2")
b_q3 = InlineKeyboardButton(text="Можно ли оплатить при получение?", callback_data="q3")
b_q4 = InlineKeyboardButton(text="Что делать если не подошел размер?", callback_data="q4")
b_q5 = InlineKeyboardButton(text="Как считать доставку за несколько вещей?", callback_data="q5")



q_keyboard = InlineKeyboardMarkup(inline_keyboard=[[b_q1], [b_q2], [b_q3], [b_q4], [b_q5], [b_to_menu]])