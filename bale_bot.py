from flask import Flask
from threading import Thread
from bale import Bot
import os

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

@bot.event
async def on_message(message):
    text = getattr(message, "text", "")

    if text == "/start":
        await message.reply("سلام 👋\n\nبه ربات خوش آمدید.")

print("Bot Started...")
bot.run()
