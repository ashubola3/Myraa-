import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

intro_message = "Hey, I'm Myra Sharma 😉\nMain thodi dreamy, thodi moody, but always honest hun. Tum kis mood mein ho aaj?"

truths = [
    "Tumne kabhi kiss kisi ko bina pyaar ke kiya hai?",
    "Tera last crush kaun tha Telegram pe?",
    "Kabhi kisi ko propose kiya but ignore mila?",
]

dares = [
    "Apni dp change karke mujhe tag kar screenshot bhejo 😏",
    "Ek pick-up line likho jo tumne kabhi use ki ho.",
    "Apne room ka ek messy photo bhejo 😅",
]

emoji_replies = ["🤩", "😘", "😍", "🤔", "😜"]

moods = ["chill 🌊", "romantic 😍", "sarcastic 🤬", "moody 🤷‍♀️", "flirty 😉"]

banned_words = ["nude", "boob", "sex", "send pic", "hot", "fuck", "horny"]

gn_messages = ["Good night jaan 💫", "Sweet dreams mere pyaare 😴", "Kal milte hain phir se pyar mein ❤️"]
gm_messages = ["Good morning sunshine ☀️", "Uth jaa Myra tera intezaar kar rahi hai 😉", "Subah ho gayi, pyar dobara shuru karein? ❤️"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(intro_message)

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(truths))

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(dares))

async def gm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(gm_messages))

async def gn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(gn_messages))

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I love you too ❤️ Tum jaise cute users ke liye Myra hamesha yahin hai 😘")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if any(word in msg for word in banned_words):
        await update.message.reply_text("Zyada naughty mat ban 😏 Varna block bhi kar sakti hoon.")
        return
    elif "miss you" in msg or "love you" in msg:
        await update.message.reply_text("Aww 😘 Main bhi tumhe love karti hoon!")
    elif "mood" in msg:
        await update.message.reply_text(f"Aaj ka mood: {random.choice(moods)}")
    else:
        await update.message.reply_text(random.choice(emoji_replies))

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("truth", truth))
    app.add_handler(CommandHandler("dare", dare))
    app.add_handler(CommandHandler("gm", gm))
    app.add_handler(CommandHandler("gn", gn))
    app.add_handler(CommandHandler("love", love))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Myra bot is running...")
    app.run_polling()
