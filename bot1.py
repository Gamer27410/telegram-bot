from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

NAME, SURNAME = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Salom! 🙂 Ismingizni yozing:")
    return NAME
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Familiyangizni yozing:")
    return SURNAME

async def get_surname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    name = context.user_data.get("name", "")
    surname = update.message.text

    await update.message.reply_text(
        f"{name} {surname}, tanishganimdan xursandman 😊"
    )

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Bekor qilindi ❌ /start bosib qayta boshlang.")
    return ConversationHandler.END


def main():
    BOT_TOKEN = "8400019528:AAHj6rNy6JHIkX-7b-qOxRIIPZ6uUEPUCao"

    app = Application.builder().token(BOT_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            SURNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_surname)],
        },

        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv)

    print("Bot ishga tushdi... ✅")
    app.run_polling()


if __name__ == "__main__":
    main()
