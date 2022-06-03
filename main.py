from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "Api Token"

btnmain = KeyboardButton('Bosh Menyu 🏚')

MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnmain)

btnRandom = KeyboardButton('Encryption(Shifirlash)')
btnOther = KeyboardButton('Dscrpytion(D_shifir)')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)

key2 = KeyboardButton('+2')
key3 = KeyboardButton('+3')

pluskeybutton = ReplyKeyboardMarkup(resize_keyboard=True).add(key2, key3)

keyminus2 = KeyboardButton('-2')
keyminus3 = KeyboardButton('-3')

minuskeybutton = ReplyKeyboardMarkup(resize_keyboard=True).add(keyminus2, keyminus3)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

text = ''
text1 = ''
number = 0
number1 = 0
send_text_shifir = ''
send_text_dshifir = ''

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Hello {0.first_name}\nI Text Encryption And\nDesryption Bot".format(message.from_user),
                           reply_markup=mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    global send_text_dshifir
    global send_text_shifir
    global number1
    global number
    global text1
    global text

    # Bosh Menyu

    if message.text == 'Bosh Menyu 🏚':
        await bot.send_message(message.from_user.id, 'Bosh Menyu 🏚', reply_markup=mainMenu)

    # DShifirlashga Utish

    elif message.text == 'Dscrpytion(D_shifir)':
        send_text_dshifir = ''
        text1 = ''
        number1 += 1
        await bot.send_message(message.from_user.id, 'Textni Kiriting ✍✍✍', reply_markup=MainMenu)

    # Shifirlashga Utish

    elif message.text == 'Encryption(Shifirlash)':
        send_text_shifir = ''
        text = ''
        number += 1
        await bot.send_message(message.from_user.id, 'Textni Kiriting ✍✍✍', reply_markup=MainMenu)

    # Shifirlash Uchun Textni Saqlab Olish

    elif number == 1:
        number = 0
        text += message.text
        await bot.send_message(message.from_user.id, 'Kalit Kiriting 🔑🔑🔑\n', reply_markup=pluskeybutton)

    # DShifirlash Uchun Textni Saqlab Olish

    elif number1 == 1:
        number1 = 0
        text1 += message.text
        await bot.send_message(message.from_user.id, 'Kalit Kiriting 🔑🔑🔑\n', reply_markup=minuskeybutton)

    # 2-Kilik Shifirlash

    elif message.text == '+2':
        for i in text:
            send_text_shifir += chr(ord(i) + 2)
        await bot.send_message(message.from_user.id, send_text_shifir, reply_markup=MainMenu)

    # 3-Kilik Shifirlash

    elif message.text == '+3':
        for i in text:
            send_text_shifir += chr(ord(i) + 3)
        await bot.send_message(message.from_user.id, send_text_shifir, reply_markup=MainMenu)



    # 2-Kilik DShifirlash Yechish

    elif message.text == '-2':
        for i in text1:
            send_text_shifir += chr(ord(i) - 2)
        await bot.send_message(message.from_user.id, send_text_shifir, reply_markup=MainMenu)

    # 3-Kilik DShifirlash Yechish

    elif message.text == '-3':
        for i in text1:
            send_text_dshifir += chr(ord(i) - 3)
        await bot.send_message(message.from_user.id, send_text_dshifir, reply_markup=MainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
