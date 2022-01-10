import logging
import wikipedia
import settings
from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom wikipediadan ma`lumot qidiruvchi botga xush kelibsiz!!!")


@dp.message_handler()
async def sendInfo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu so`rov bo`yicha hech narsa topilmadi.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)