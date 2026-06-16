from bale import Bot

TOKEN = "1707286533:8RiZ3SLHubKYeU9qMV3WVWx2cKHuGVDIiMg"

bot = Bot(TOKEN)

@bot.event
async def on_message(message):
    text = getattr(message, "text", "")

    if text == "/start":
        await message.reply(
            "🎨 به ربات فارس گالری خوش آمدید\n\n"
            "1️⃣ استعلام قیمت\n"
            "2️⃣ خرید\n\n"
            "یکی از گزینه‌ها را ارسال کنید."
        )

    elif text == "استعلام قیمت":
        await message.reply(
            "📏 عرض و ارتفاع پرده را ارسال کنید.\n"
            "مثال:\n"
            "200×280"
        )

    elif text == "خرید":
        await message.reply(
            "🛒 برای خرید با پشتیبانی تماس بگیرید."
        )

print("Bot Started...")
bot.run()
