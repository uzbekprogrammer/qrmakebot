import pyqrcode
from aiogram.types import InputFile


async def qrcode(name, user_id):
    # Generate QR code
    name_photo = f"{user_id}.png"
    url = pyqrcode.create(name)

    url.png(name_photo, scale=6)
    photo_file = InputFile(path_or_bytesio=name_photo)

    return photo_file


if __name__ == '__main':
    qrcode("https://www.youtube.com/", "yt")
    qrcode("https://github.com/", "gk")
