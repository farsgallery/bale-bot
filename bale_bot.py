from bale import Bot, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "YOUR_BALE_TOKEN"

bot = Bot(TOKEN)

@bot.event
async def on_message(message):
    if message.text == "/start":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💰 استعلام قیمت", callback_data="price")],
            [InlineKeyboardButton("🛒 خرید", callback_data="buy")]
        ])

        await message.reply(
            "🎨 به ربات فارس گالری خوش آمدید",
            components=keyboard
        )

@bot.callback_query()
async def callbacks(query):
    if query.data == "price":
        await query.message.reply("لطفاً نوع پرده را انتخاب کنید.")
    elif query.data == "buy":
        await query.message.reply("لطفاً اطلاعات سفارش را ارسال کنید.")

bot.run()
