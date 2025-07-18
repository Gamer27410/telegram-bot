from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# --- Tugmali menyu
menu = [["Mehr", "Ramantika", "Erkalash"]]
markup = ReplyKeyboardMarkup(menu, resize_keyboard=True, one_time_keyboard=True)

# --- /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "GAVHARIM mendan nima eshitishni xohlaydi😊😘🫠🥰😍😍🙂❤️‍🔥💖🫶",
        reply_markup=markup
    )

# --- Javoblar funksiyasi
async def javoblar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    matn = update.message.text.lower()

    if "mehr" in matn:
        await update.message.reply_text("Mening tanho oppoqina yuzli😊,uzun sochli🥰 sevgilim❤️...", reply_markup=ReplyKeyboardRemove())
    elif "ramantika" in matn:
        await update.message.reply_text("Siz bilan ramantika qilishga hali kop vaqtimiz boladi...", reply_markup=ReplyKeyboardRemove())
    elif "erkalash" in matn:
        await update.message.reply_text("Shirin yuzli ponchigim🫠 sizni tishlab olgim keladi...", reply_markup=ReplyKeyboardRemove())
    else:
        await update.message.reply_text("Iltimos, tugmalardan birini tanlang.", reply_markup=markup)

# --- Botni ishga tushurish
TOKEN = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, javoblar))

app.run_polling()
