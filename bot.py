from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = "1922222846:AAF3N79qHJTmuIJd_XRUyMQBdtwa3jDjnmY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Я бот. приветики,{msg.from_user.first_name}')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Гутен морген!')
    else:
        await msg.answer('Ась?')

if __name__ == '__main__':
    executor.start_polling(dp)
