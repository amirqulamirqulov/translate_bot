from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Tilni tanlang!")
kb.add(btn1)


ikb = InlineKeyboardMarkup(row_width=3)
ikb1 = InlineKeyboardButton(text="Uzbek 🇺🇿",
                            callback_data="uz")
ikb2 = InlineKeyboardButton(text="English 󠁧🇬🇧",
                            callback_data="en")
ikb3 = InlineKeyboardButton(text="Russian 🇷🇺",
                            callback_data="ru")
ikb4 = InlineKeyboardButton(text="Japan 🇯🇵",
                            callback_data="ja")
ikb5 = InlineKeyboardButton(text="Korean 🇰🇷󠁧󠁢󠁥󠁮󠁧󠁿",
                            callback_data="ko")
ikb6 = InlineKeyboardButton(text="French 🇫🇷",
                            callback_data="fr")
ikb7 = InlineKeyboardButton(text="Spanish 🇪🇸",
                            callback_data="es")
ikb8 = InlineKeyboardButton(text="German 🇩🇪󠁧󠁢󠁥󠁮󠁧󠁿",
                            callback_data="de")
ikb9 = InlineKeyboardButton(text="Turkey 🇹🇷",
                            callback_data="tr")
ikb10 = InlineKeyboardButton(text="Italy 🇮🇹",
                             callback_data="it")
ikb11 = InlineKeyboardButton(text="Arab 🇦🇪",
                             callback_data="ar")
ikb12 = InlineKeyboardButton(text="Cina 🇨🇳",
                             callback_data="zh")

ikb.add(ikb1, ikb2, ikb3)
ikb.add(ikb4, ikb5, ikb6)
ikb.add(ikb7, ikb8, ikb9)
ikb.add(ikb10, ikb11, ikb12)
