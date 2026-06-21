from bale import Bot, Message
from bale.handlers import CommandHandler, MessageHandler
from bale.checks import TEXT
import datetime

client = Bot(token="1707286533:SfrV0VrqFr5qWoUC3O-Pte121jWlzA8W3dM")

# قیمت‌ها
PRICES = {
    "shid_simple": 1980000,
    "shid_blackout": 3350000,
    "zebra": 2325000,
    "cercere": 2970000
}

# منوی اصلی
MAIN_MENU = """
به ربات مجموعه هُنری فــارس گـالری خوش آمدید
میتوانید برای استعلام قیمت بر اساس ابعاد و اندازه پرده مورد نظر خود و همچنین ثبت سفارش از این ربات به راحتی استفاده کنید:
"""

# منوی استعلام قیمت
PRICE_MENU = """
📊 **استعلام قیمت پرده**

1️⃣ پرده شید ساده
2️⃣ پرده شید بلک اوت
3️⃣ پرده زبرا
4️⃣ پرده کرکره فلزی

🔙 بازگشت
"""

# منوی رنگ‌ها
COLOR_MENU = """
🎨 **انتخاب رنگ**

1️⃣ سفید
2️⃣ طوسی
3️⃣ کرم
4️⃣ مشکی
5️⃣ قهوه‌ای

🔙 بازگشت
"""

# منوی تماس با ما
CONTACT_MENU = """
📞 **تماس با ما**

📍 آدرس: شیراز خیابان قصردشت چهارراه عفیف آباد ابتدای بلوار آوینی نبش کوچه یک مجموعه گالری هنری ایران دکوراسیون (فارس گالری)

📱 شماره تماس: 07136277172

⏰ ساعات کاری:
🌅 صبح: 09:00 تا 13:00
🌆 عصر: 17:00 تا 21:00

🌐 وب‌سایت: [www.FarsGallery.com](http://www.farsgallery.com/)

🔙 بازگشت
"""

# منوی راهنمایی
GUIDE_MENU = """
💡 **راهنمایی و پیشنهاد نوع پرده**

1️⃣ اداری و تجاری
2️⃣ مسکونی

🔙 بازگشت
"""

# منوی ثبت سفارش
ORDER_MENU = """
🛒 **ثبت سفارش**

1️⃣ پرده شید ساده
2️⃣ پرده شید بلک اوت
3️⃣ پرده زبرا
4️⃣ پرده کرکره فلزی

🔙 بازگشت
"""

# منوی شروع
START_MENU = """
🚀 **شروع**

1️⃣ استعلام قیمت
2️⃣ ثبت سفارش
3️⃣ راهنمایی و پیشنهاد
4️⃣ تماس با ما

🔙 خروج
"""

# منوی تکرار محاسبه
RECALC_MENU = """
🔄 **تکرار محاسبه**

1️⃣ بله، دوباره حساب کن
2️⃣ خیر، منو را باز کن

🔙 بازگشت
"""

# منوی انتخاب نوع پرده برای ثبت سفارش
ORDER_TYPE_MENU = """
🛒 **ثبت سفارش**

1️⃣ پرده شید ساده
2️⃣ پرده شید بلک اوت
3️⃣ پرده زبرا
4️⃣ پرده کرکره فلزی

🔙 بازگشت
"""

# لینک‌ها
LINKS = {
    "shid_simple": "https://farsgallery.com/product-category/curtains/shid/",
    "shid_blackout": "https://farsgallery.com/product-category/curtains/shid/",
    "zebra": "https://farsgallery.com/product-category/curtains/zebra/simple/",
    "cercere": "https://farsgallery.com/product-category/curtains/cercere/25mil/"
}

# منوهای دکمه‌ای
def get_main_keyboard():
    return [
        [MessageHandler("1️⃣ استعلام قیمت", price_menu)],
        [MessageHandler("2️⃣ ثبت سفارش", order_menu)],
        [MessageHandler("3️⃣ راهنمایی و پیشنهاد", guide_menu)],
        [MessageHandler("4️⃣ تماس با ما", contact_menu)],
        [MessageHandler("🔙 خروج", exit_bot)]
    ]

def get_price_keyboard():
    return [
        [MessageHandler("1️⃣ پرده شید ساده", shid_simple_calc)],
        [MessageHandler("2️⃣ پرده شید بلک اوت", shid_blackout_calc)],
        [MessageHandler("3️⃣ پرده زبرا", zebra_calc)],
        [MessageHandler("4️⃣ پرده کرکره فلزی", cercere_calc)],
        [MessageHandler("🔙 بازگشت", main_menu)]
    ]

def get_color_keyboard():
    return [
        [MessageHandler("1️⃣ سفید", select_color)],
        [MessageHandler("2️⃣ طوسی", select_color)],
        [MessageHandler("3️⃣ کرم", select_color)],
        [MessageHandler("4️⃣ مشکی", select_color)],
        [MessageHandler("5️⃣ قهوه‌ای", select_color)],
        [MessageHandler("🔙 بازگشت", price_menu)]
    ]

def get_guide_keyboard():
    return [
        [MessageHandler("1️⃣ اداری و تجاری", commercial_type)],
        [MessageHandler("2️⃣ مسکونی", residential_type)],
        [MessageHandler("🔙 بازگشت", main_menu)]
    ]

def get_order_keyboard():
    return [
        [MessageHandler("1️⃣ پرده شید ساده", order_shid_simple)],
        [MessageHandler("2️⃣ پرده شید بلک اوت", order_shid_blackout)],
        [MessageHandler("3️⃣ پرده زبرا", order_zebra)],
        [MessageHandler("4️⃣ پرده کرکره فلزی", order_cercere)],
        [MessageHandler("🔙 بازگشت", main_menu)]
    ]

def get_order_type_keyboard():
    return [
        [MessageHandler("1️⃣ پرده شید ساده", order_shid_simple)],
        [MessageHandler("2️⃣ پرده شید بلک اوت", order_shid_blackout)],
        [MessageHandler("3️⃣ پرده زبرا", order_zebra)],
        [MessageHandler("4️⃣ …
