from flask import Flask
from threading import Thread
from bale import Bot
import os

TOKEN = "1707286533:8RiZ3SLHubKYeU9qMV3WVWx2cKHuGVDIiMg"

app = Flask(__name__)

@app.route("/")
def home():
return "Bale Bot Running"

def run_web():
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()

bot = Bot(TOKEN)

@bot.event
async def on_message(message):
text = getattr(message, "text", "")

```
if text == "/start":
    await message.reply(
        "🎨 به ربات فارس گالری خوش آمدید\n\n"
        "💰 استعلام قیمت\n"
        "🛒 خرید\n\n"
        "یکی از گزینه‌ها را تایپ کنید."
    )

elif text == "استعلام قیمت":
    await message.reply(
        "لطفاً نوع پرده و ابعاد را ارسال کنید."
    )

elif text == "خرید":
    await message.reply(
        "لطفاً اطلاعات سفارش را ارسال کنید."
    )
```

print("Bot Started...")
bot.run()
