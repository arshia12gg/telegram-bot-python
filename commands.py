from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# توکن ربات خود را اینجا وارد کنید
BOT_TOKEN = '7659692029:AAFUc6aEkobCqdA8iQ4peCd2mT8BiCzAark'

# دیکشنری برای ذخیره حالت کاربرها
user_state = {}

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("شروع⭐", callback_data='start_reply')],
        [InlineKeyboardButton("کانال ما ⚡", url='https://t.me/axerdns')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('به ربات خوش آمدید 🌹\nکارایی:\nجوابگو در پی‌وی', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'start_reply':
        user_id = query.from_user.id
        user_state[user_id] = 'waiting_for_message'
        query.message.reply_text("متنی که می‌خواهید در پی‌وی ارسال شود را وارد کنید:")

def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    if user_id not in user_state:
        return

    state = user_state[user_id]

    if state == 'waiting_for_message':
        context.user_data['auto_reply'] = update.message.text
        user_state[user_id] = 'waiting_for_phone'
        update.message.reply_text("شماره خود را وارد کنید ✅\nمثال: +989309174512")

    elif state == 'waiting_for_phone':
        phone = update.message.text
        context.user_data['phone_number'] = phone
        user_state[user_id] = 'done'
        update.message.reply_text("فعلاً نمی‌توانیم کد ورود ارسال کنیم چون این عملیات خلاف قوانین ربات‌ها است.\nاما پیام خودکار ذخیره شد.")

def auto_reply(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    if update.message.chat.type == 'private':
        if 'auto_reply' in context.user_data:
            update.message.reply_text(context.user_data['auto_reply'])

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(MessageHandler(Filters.private & Filters.text, auto_reply))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
