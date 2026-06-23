# bale_bot_fixed.py

async def show_main_menu(message):
    await message.reply(
        "یکی از گزینه‌ها را بنویس:\n"
        "1- استعلام قیمت\n"
        "2- ثبت سفارش\n"
        "3- تماس با ما"
    )
