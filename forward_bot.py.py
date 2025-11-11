from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# 🔐 Твой токен
TOKEN = "ВАШ_НОВЫЙ_ТОКЕН"

# 📥 Группа, где бот ищет сообщения
SOURCE_CHAT_ID = -1001946191112  # группа-источник

# 📤 Группа, куда пересылать
TARGET_CHAT_ID = -1001984134879  # группа-получатель

# 🎯 Фраза для поиска
TARGET_PHRASE = "Мы собрали все предложения по заявке на оценку"

async def check_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    text = message.text or message.caption or ""
    if TARGET_PHRASE.lower() in text.lower():
        await message.forward(chat_id=TARGET_CHAT_ID)
        print("✅ Сообщение переслано")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    handler = MessageHandler(filters.Chat(chat_id=SOURCE_CHAT_ID), check_messages)
    app.add_handler(handler)

    print("🤖 Бот запущен и слушает группу")
    app.run_polling()

if __name__ == "__main__":
    main()
