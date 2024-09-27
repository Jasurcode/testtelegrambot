from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import html

from loader import dp
from states.registerStates import RegistrationStates
from keyboards.default.registerkeyboards import ask_phone
from data.saveData import checkUser
from keyboards.default.menukeyboardd import menu

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/start` command
    """
    if not checkUser(message.from_user.id):
        await message.answer(f"Salom, {html.bold(message.from_user.full_name)}\n"
                             f"Royxatdan otish uchun telefon raqam kiriting!", reply_markup=ask_phone)
        await state.set_state(RegistrationStates.phone)

    else:
        await message.answer(f"Quyidagi menyudan kerakli bolimni tanlang!", reply_markup=menu)





