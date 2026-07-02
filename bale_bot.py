from flask import Flask
from threading import Thread
from bale import Bot
import os
import jdatetime

TOKEN = "1707286533:SfrV0VrqFr5qWoUC3O-Pte121jWlzA8W3dM"

app = Flask(__name__)


@app.route("/")
def home():
    return "Bale Bot Running"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


Thread(target=run_web).start()

bot = Bot(TOKEN)


def get_today():
    return jdatetime.datetime.now().strftime("%Y/%m/%d")


MAIN_MENU = """
🎨 به ربات مجموعه هنری فارس گالری خوش آمدید

می‌توانید برای استعلام قیمت بر اساس ابعاد و اندازه پرده مورد نظر خود و همچنین ثبت سفارش از این ربات استفاده کنید.

📅 تاریخ امروز: {}

━━━━━━━━━━━━━━

1️⃣ میخواهم فقط استعلام قیمت پرده بگیرم

2️⃣ میخواهم ثبت سفارش انجام بدم

📞 آدرس و تماس با ما

💡 راهنمایی و پیشنهاد نوع پرده

🔄 شروع مجدد
"""


CONTACT_TEXT = """
📍 آدرس:

شیراز خیابان قصردشت
چهارراه عفیف آباد
ابتدای بلوار آوینی
نبش کوچه یک
مجموعه گالری هنری ایران دکوراسیون
(فارس گالری)

☎️ شماره تماس:
07136277172

🕘 ساعات کاری:

صبح:
09:00 تا 13:00

عصر:
17:00 تا 21:00

🌐 وب سایت خرید آنلاین:

www.FarsGallery.com
"""


GUIDE_TEXT = """
💡 برای چه کاربری میخواهید؟

1️⃣ اداری و تجاری

2️⃣ مسکونی
"""


@bot.event
async def on_message(message):

    text = getattr(message, "text", "")

    if text in ["/start", "🔄 شروع مجدد"]:

        await message.reply(MAIN_MENU.format(get_today()))

    elif text == "📞 آدرس و تماس با ما":

        await message.reply(CONTACT_TEXT)

    elif text == "💡 راهنمایی و پیشنهاد نوع پرده":

        await message.reply(GUIDE_TEXT)

    elif text == "1️⃣ اداری و تجاری":

        await message.reply(
            "🏢 پیشنهاد ما:\n\nپرده کرکره فلزی\n\n(در مرحله بعد مستقیماً وارد محاسبه قیمت می‌شود)"
        )

    elif text == "2️⃣ مسکونی":

        await message.reply(
            "🏠 پیشنهاد ما:\n\n• پرده شید ساده\n• پرده زبرا\n\n(در مرحله بعد مستقیماً وارد محاسبه قیمت می‌شود)"
        )

    elif text == "1️⃣ میخواهم فقط استعلام قیمت پرده بگیرم":

        await message.reply(
            """
🪟 نوع پرده را انتخاب کنید:

• پرده شید ساده

• پرده شید بلک اوت

• پرده زبرا

• پرده کرکره فلزی
"""
        )

    elif text == "2️⃣ میخواهم ثبت سفارش انجام بدم":

        await message.reply(
            """
🛒 ثبت سفارش

در مرحله بعد لینک محصولات اضافه خواهد شد.
"""
        )


print("Bot Started...")
bot.run()
