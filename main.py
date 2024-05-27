from aiogram import Bot, Dispatcher, types, executor

from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы загрузить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь наш бот'),
        types.BotCommand(command='/information', description='Команда которая выводит что умеет бот'),
        types.BotCommand(command='/pops', description='Команда которая выводит любимую музыку бота'),
        types.BotCommand(command='/food', description='Команда которая выводит любимую еду бота'),
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я ЭХО бот')


@dp.message_handler(commands='help')
async def start(message: types.Message):
    await message.reply('Я могу помочь тебе.....')


@dp.message_handler(commands='information')
async def start(message: types.Message):
    await message.reply('Я ЭХО бот, умею повторять за тобой и многое другое')


@dp.message_handler(commands='pops')
async def start(message: types.Message):
    await message.reply('Это моя любимая музыка.....')


@dp.message_handler(commands='food')
async def start(message: types.Message):
    await message.reply('Это моя любимая еда.....')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

