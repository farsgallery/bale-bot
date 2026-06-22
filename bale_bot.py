import asyncio
import math
from datetime import datetime

from bale import Bot, Message, Update
from bale.handlers import CommandHandler
from bale.checks import Author, TEXT

TOKEN = "1707286533:SfrV0VrqFr5qWoUC3O-Pte121jWlzA8W3dM"

client = Bot(token=TOKEN)

# -----------------------------
# اطلاعات فروشگاه
# -----------------------------

ADDRESS = """
📍 آدرس:
شیراز، خیابان قصردشت، چهارراه عفیف آباد،
ابتدای بلوار آوینی، نبش کوچه 1
مجموعه هنری ایران دکوراسیون (فارس گالری)
"""

PHONE = "☎️ 07136277172"

WORK_TIME = """
🕒 ساعات کاری:
صبح: 09:00 تا 13:00
عصر: 17:00 تا 21:00
"""

WEBSITE = "🌐 www.FarsGallery.com"

# -----------------------------
# محصولات
# -----------------------------

PRODUCTS = {
    "شید ساده": {
        "price": 1980000,
        "min_height": 200,
        "min_area": 2,
        "colors": ["⚪ سفید", "🔘 طوسی", "🟤 کرم"]
    },
    "شید بلک اوت": {
        "price": 3350000,
        "min_height": 200,
        "min_area": 2,
        "colors": ["⚪ سفید", "🔘 طوسی", "🟤 کرم"]
    },
    "زبرا": {
        "price": 2325000,
        "min_height": 150,
        "min_area": 1.5,
        "colors": ["⚪ سفید", "🔘 طوسی", "🟤 قهوه ای"]
    },
    "کرکره فلزی": {
        "price": 2970000,
        "min_height": 0,
        "min_area": 1.5,
        "colors": ["⚪ سفید", "🔘 طوسی", "⚫ مشکی"]
    }
}


# -----------------------------
# ابزارها
# -----------------------------

def today():
    return datetime.now().strftime("%Y/%m/%d")


def format_price(num):
    return "{:,}".format(int(num))


async def ask_text(message, text):
    await message.reply(text)

    update = await client.wait_for(
        Author(message.author.id) & TEXT,
        timeout=300
    )

    return update.message.text


async def calculate_price(message, product_name):

    data = PRODUCTS[product_name]

    width = await ask_text(
        message,
        f"📏 عرض {product_name} را به سانتیمتر وارد کنید:"
    )

    height = await ask_text(
        message,
        f"📐 ارتفاع {product_name} را به سانتیمتر وارد کنید:"
    )

    try:
        width = float(width)
        height = float(height)
    except:
        return await message.reply("❌ فقط عدد وارد کنید.")

    notes = []

    original_height = height

    if data["min_height"] > 0 and height < data["min_height"]:
        notes.append(
            f"⚠️ طبق قوانین {product_name} ارتفاع کمتر از "
            f"{data['min_height']} سانتیمتر محاسبه نمی‌شود "
            f"و {data['min_height']} در نظر گرفته شد."
        )

        height = data["min_height"]

    area = (width * height) / 10000

    if area < data["min_area"]:
        notes.append(
            f"⚠️ طبق قوانین {product_name} حداقل متراژ "
            f"{data['min_area']} متر مربع محاسبه می‌شود."
        )

        area = data["min_area"]

    final_price = area * data["price"]

    text = f"""
📅 تاریخ: {today()}

🪟 نوع پرده: {product_name}

📏 عرض: {width:.0f} سانتیمتر
📐 ارتفاع وارد شده: {original_height:.0f} سانتیمتر
📐 ارتفاع محاسبه شده: {height:.0f} سانتیمتر

📦 متراژ نهایی:
{area:.2f} متر مربع

💰 قیمت واحد:
{format_price(data['price'])} تومان

💵 قیمت نهایی:
{format_price(final_price)} تومان
"""

    if notes:
        text += "\n\n" + "\n".join(notes)

    text += """

━━━━━━━━━━━━━━

🚚 سه روز کاری تحویل

📦 ارسال به سراسر کشور

🛡️ 2 سال ضمانت

😍 کیفیت درجه یک
دیگه چی میخوای؟ 😍

اگر مایل هستید رنگ بندی را مشاهده کنید
کلمه زیر را ارسال کنید:

🎨 رنگ بندی
"""

    await message.reply(text)

    color_request = await ask_text(
        message,
        "🎨 برای مشاهده رنگ بندی بنویس:\nرنگ بندی"
    )

    if "رنگ" in color_request:

        colors = "\n".join(data["colors"])

        await message.reply(
            f"🎨 رنگ های موجود {product_name}\n\n{colors}"
        )

    await message.reply(
        "🔄 برای محاسبه مجدد /start را ارسال کنید."
    )


# -----------------------------
# شروع
# -----------------------------

@client.listen("on_ready")
async def ready():
    print(client.user, "READY")


@client.handle(CommandHandler("start"))
async def start(message: Message):

    text = f"""
🎨 به ربات مجموعه هنری فارس گالری خوش آمدید

📅 تاریخ امروز:
{today()}

برای ادامه یکی از گزینه های زیر را ارسال کنید:

1️⃣ استعلام قیمت

2️⃣ ثبت سفارش

3️⃣ راهنمای انتخاب پرده

4️⃣ تماس با ما
"""

    await message.reply(text)

    try:
        update = await client.wait_for(
            Author(message.author.id) & TEXT,
            timeout=300
        )
    except:
        return

    choice = update.message.text

    # -----------------------------------
    # استعلام قیمت
    # -----------------------------------

    if "1" in choice or "استعلام" in choice:

        await update.message.reply("""
🪟 نوع پرده را انتخاب کنید:

1- شید ساده
2- شید بلک اوت
3- زبرا
4- کرکره فلزی
""")

        update2 = await client.wait_for(
            Author(message.author.id) & TEXT,
            timeout=300
        )

        product = update2.message.text

        if "1" in product or "شید ساده" in product:
            await calculate_price(update2.message, "شید ساده")

        elif "2" in product or "بلک" in product:
            await calculate_price(update2.message, "شید بلک اوت")

        elif "3" in product or "زبرا" in product:
            await calculate_price(update2.message, "زبرا")

        elif "4" in product or "کرکره" in product:
            await calculate_price(update2.message, "کرکره فلزی")

    # -----------------------------------
    # راهنما
    # -----------------------------------

    elif "3" in choice or "راهنما" in choice:

        await update.message.reply("""
🏠 نوع کاربری را انتخاب کنید:

1- مسکونی
2- اداری / تجاری
""")

        update3 = await client.wait_for(
            Author(update.message.author.id) & TEXT,
            timeout=300
        )

        answer = update3.message.text

        if "اداری" in answer or "2" in answer:

            await update3.message.reply("""
🏢 پیشنهاد ما:

🪟 پرده کرکره فلزی

برای استعلام قیمت:
/start
""")

        else:

            await update3.message.reply("""
🏠 پیشنهاد ما:

🪟 پرده شید ساده

یا

🪟 پرده زبرا

برای استعلام قیمت:
/start
""")

    # -----------------------------------
    # ثبت سفارش
    # -----------------------------------

    elif "2" in choice or "ثبت سفارش" in choice:

        await update.message.reply("""
🛒 نوع پرده را انتخاب کنید:

1- شید ساده (پیشنهاد مسکونی)

2- شید بلک اوت
(پیشنهاد اتاق کامپیوتر و ویدیو پروژکتور)

3- زبرا (پیشنهاد مسکونی)

4- کرکره فلزی
(پیشنهاد اداری و تجاری)
""")

        update4 = await client.wait_for(
            Author(update.message.author.id) & TEXT,
            timeout=300
        )

        p = update4.message.text

        if "1" in p:
            await update4.message.reply(
                "🔗 لینک محصول شید ساده:\nYOUR_LINK"
            )

        elif "2" in p:
            await update4.message.reply(
                "🔗 لینک محصول شید بلک اوت:\nYOUR_LINK"
            )

        elif "3" in p:
            await update4.message.reply(
                "🔗 لینک محصول زبرا:\nYOUR_LINK"
            )

        elif "4" in p:
            await update4.message.reply(
                "🔗 لینک محصول کرکره فلزی:\nYOUR_LINK"
            )

    # -----------------------------------
    # تماس با ما
    # -----------------------------------

    elif "4" in choice or "تماس" in choice:

        await update.message.reply(
            f"{ADDRESS}\n\n{PHONE}\n\n{WORK_TIME}\n\n{WEBSITE}"
        )


client.run()
