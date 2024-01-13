import asyncio, logging, sys, requests
from os import getenv

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram import Dispatcher, Bot, filters
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from bs4 import BeautifulSoup


dp = Dispatcher(storage=MemoryStorage())

BOT_TOKEN = "6876133315:AAFbdWJf1u9ASPrrdWI76Pcxzu1I85deCYg"
class Menu(StatesGroup):
    news = State()


def menu_buttons():
    new_post = KeyboardButton(text="New Posts 📨")
    return ReplyKeyboardMarkup(keyboard=[[new_post]], resize_keyboard=True, one_time_keyboard=True)


@dp.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(f"Hello - 👤 {msg.from_user.full_name}")
    print(f"👤 - {msg.from_user.full_name}")
    await msg.answer(f"Assalomu alaykum\n\nBot yordamida millionlab odamlarni qiynaydigan Nima ovqat qilay ? \n degan savolga oson javob oling️", reply_markup=menu_buttons())
    await state.set_state(Menu.news)


@dp.message(Menu.news)
async def menu_handler(msg: Message, state: FSMContext):
    response = requests.get("https://kun.uz/")
    soup = BeautifulSoup(response.text, 'html.parser')

    for i in soup.find_all("div", 'col-md-4'):
        img = i.find("img")['src']
        txt1 = i.find("span").text
        txt2 = i.find("a", "news__title").text
        await msg.answer_photo(f"{img}", caption=f"\n{txt1}\n\n{txt2}")


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())