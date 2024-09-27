from http.client import responses

from aiogram.types import Message
from loader import dp, bot
from bot.utils.gptrequest import send_request

@dp.message()
async def echo_handler(message: Message) -> None:
    await bot.send_chat_action(message.chat.id, "typing")
    text = message.text
    response = send_request(text)
    await message.answer(response)