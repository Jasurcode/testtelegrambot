from cmath import phase

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data.saveData import saveUser
from loader import dp
from states.registerStates import RegistrationStates
from keyboards.default.menukeyboardd import menu


@dp.message(RegistrationStates.phone)
async def registrationPhone(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    elif message.text:
        phone = message.text
    else:
        phone = None
    await state.update_data(phone=phone)

    await message.answer("Emailingizni yuboring: ")
    await state.set_state(RegistrationStates.email)


@dp.message(RegistrationStates.email)
async def registrationemail(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    username = message.from_user.username if message.from_user.username else None
    saveUser(user_id, user_fullname, username, data['email'], data['phone'])
    await state.clear()
    await message.answer("Ro'yxatdan o'tdingiz", reply_markup=menu)


