import logging
import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from app.config import BOT_TOKEN, DATABASE_URL, API_URL


token = "7310659744:AAFhI2W_-nzzLcmGXgnpFXY-J741VPfMw9s"
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    pho = [
        [types.KeyboardButton(text="send contact!")]
    ]
    button = types.ReplyKeyboardMarkup(keyboard=pho, resize_keyboard=True, request_contact=True)
    await message.answer("iltimos telefon raqam yuboring", reply_markup=button)




@dp.message(Command("contact"))
async def contact_handler(message: types.Message):
    phone_number = message.contact.phone_number
    telegram_id = message.from_user.id

    response = requests.post(f"{API_URL}/register", json={
        "telegram_id": telegram_id,
        "phone_number": phone_number
    })

    if response.status_code == 200:
        await message.answer("Tasdiqlash kodi yuborildi! Endi /verify 123456 shaklida kodni kiriting.")
    else:
        await message.answer("Xatolik yuz berdi, qayta urinib ko‘ring.")




@dp.message(Command("verify"))
async def verify_handler(message: types.Message):
    try:
        _, code = message.text.split()
        telegram_id = message.from_user.id

        response = requests.post(f"{API_URL}/verify", json={
            "telegram_id": telegram_id,
            "verification_code": code
        })

        if response.status_code == 200:
            await message.answer("✅ Muvaffaqiyatli tasdiqlandi!")
        else:
            await message.answer("❌ Noto‘g‘ri yoki eskirgan kod.")
    except Exception as e:
        await message.answer("❗ Kodni to‘g‘ri formatda kiriting: /verify 123456")



async def main() -> None:
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


