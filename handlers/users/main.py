from aiogram import types
# from makePart import qrcode
from handlers.users.makePart import qrcode
from loader import dp
import os


@dp.message_handler()
async def mainhandler(message: types.Message):
    # print(message)
    user = message.from_user.id
    msg = message.text
    # print(msg)
    # print(user)
    answer = await message.answer("Iltimos biroz kuting ...")

    photo = await qrcode(msg, user)
    await message.answer_photo(photo, caption="""🔳@QRmakebot""")
    await answer.delete()
    os.remove(f"{user}.png")
