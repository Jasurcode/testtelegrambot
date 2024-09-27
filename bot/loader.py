from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from data import config
from openai import OpenAI
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

from data.config import CHATGPT_TOKEN
client = OpenAI(api_key=CHATGPT_TOKEN)
