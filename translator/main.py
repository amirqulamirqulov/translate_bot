from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
from translate_function import translation
from keyboards import ikb, kb
from aiogram.dispatcher.filters import Text

bot = Bot(token=TOKEN_API)
db = Dispatcher(bot=bot)

HELP_COMMAND = """
<b>/start</b> - <em>Botimizni ishga tushiradi</em>
<b>/help</b> - <em>Komandalar ro'yxatini ko'rsatadi</em>
<b>/description</b> - <em>Botimiz siz kiritgan ixtiyoriy so'zni belgilangan tilga tarjima qilib beradi.</em>"""


async def on_startup(_):
    print("Kodimiz muvaffaqiyatli kompilyatsiya qilindi.")


@db.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text='Xush kelibsiz bizning botga! 👨‍💻',
                         reply_markup=kb)
    await message.delete()


@db.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")
    await message.delete()


@db.message_handler(commands=['description'])
async def command_desc(message: types.Message):
    await message.answer(text="Botimiz siz kiritgan ixtiyoriy so'zni belgilangan tilga tarjima qilib beradi.", )
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAEIhU9kMuUvqahdMyXNIJMUhYc4CFqHhwACewAD9wLID0X7aCG8iMvfLwQ")
    await message.delete()


@db.message_handler(Text(equals="Tilni tanlang!"))
async def select_language(message: types.Message):
    await message.answer(text="Tilni tanlang!",
                         reply_markup=ikb)


tr_lg = ""


@db.callback_query_handler()
async def language(callback: types.CallbackQuery):
    global tr_lg
    tr_lg = callback.data
    await callback.message.answer(text="Til tanlandi!\nMatn kiritishingiz mumkin.")
    await callback.message.delete()
    await callback.answer()


@db.message_handler()
async def translate(message: types.Message):
    global tr_lg
    translated_text = translation(message.text, tr_lg)
    await message.answer(text=translated_text,
                         reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dispatcher=db,
                           on_startup=on_startup,
                           skip_updates=True)
