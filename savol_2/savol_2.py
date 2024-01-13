import asyncio
import logging
import random
import sys

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

BOT_TOKEN = "6876133315:AAFbdWJf1u9ASPrrdWI76Pcxzu1I85deCYg"
dp = Dispatcher(storage=MemoryStorage())


class Menu(StatesGroup):
    menu = State()


def menu_button():
    random = InlineKeyboardButton(text='Random 🍗', callback_data='random')
    help = InlineKeyboardButton(text="Help 📄", callback_data='help')
    design = [
        [random, help]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


@dp.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(f"Hello - 👤 {msg.from_user.full_name}")
    await msg.answer('Assalomu alaykum  \n\n Bot yordamida millionlab odamlarni qiynaydigan " Nima ovqat qilay" ?  degan savolga oson javob oling️',
                     reply_markup=menu_button())
    await state.set_state(Menu.menu)


products = [
    "Baliqli uch panja\n\nMASALLIQLAR\nkungaboqar yog'i - 100 gr\ntuz - 1 ta'bga ko'ra\nbaliq - 1 kg\nziravor - 1 ta'bga ko'ra\nlimon - 1 dona",
    "Tovuq pishirish\n\nMASALLIQLAR\nkungaboqar yog'i - 1 stakan\nun - ta'bga ko'ra\ntuz - 0,5 choy qoshiq\nsarimsoqpiyoz donasi - 1 dona\ntovuq boldiri - 3-4 dona\npektin - murch- bir chimdim"
    "Osh\n\n1 kg guruch\n1 kg qo’y go’shti\n1 kg sabzi\n300 ml o’simlik moyi\n4 ta o’rtacha piyoz\n2 ta achchiq qalampir\n2 bosh sarimsoq\n1 osh qoshiq zira\n1 choy qoshiq kashnich urug’lari\nta’bga ko’ra tuz.",
    "RATATUY \n\n  MASALLIQLAR\npiyoz - 2 dona\nbaqlajon - 1 dona\npomidor - 1 kg\nbulg'or qalampir - 2 dona\ntuz - 1 osh qoshiq\nqovoq - 1 kg\nrayhon - 5 dona\nsarimsoqpiyoz donasi - 3 dona\nlimon - 1 dona\nzaytun yog'i - 0.5 stakan\nkashnich (kinza) - 0.5 bog‘",
    "Gamburger 🍔 \n\n MASALLIQLAR\npiyoz - 1 dona\npomidor - 1 dona\nbodring - 1 dona\npishloq - 4 dona\nmayonez - ta'bga ko'ra\nmol go'shti qiymasi - ta'bga ko'ra\nsalat bargi - 4 dona\nketchup - ta'bga ko'ra"]


@dp.callback_query(lambda call: call.data in ('random', 'help'), Menu.menu)
async def menu_handler(call: CallbackQuery, state: FSMContext):
    if call.data == "random":
        txt = products[random.randrange(0, 4)]
        await call.message.answer(txt, reply_markup=menu_button())
        await state.set_state(Menu.menu)
    elif call.data == "help":
        await call.message.answer("Tugmalardan birini tanlang ⤵️", reply_markup=menu_button())
        await state.set_state(Menu.menu)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())