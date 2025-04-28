from telegram import _update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
from typing import final
from kingdoms import messages
from handles_responding import responses ,results_command
from authorization import *

TOKEN: final = ''
BOT_NAME: final = 'Kobe_kingdom_bot'

async def start_command(update: _update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.chat.id
    users = [zeryd, para, mo, daadir, mado, sol]
    if (update.message.chat.id) == -4058770155 or (authorized_users(user, users)):
        await update.message.reply_text("Welcome to the kingdom game bot!!, press here /help to understand more on how the bot works.")
    if (update.message.chat.type) != "private":
        return False
async def help_command(update: _update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.chat.id
    users = [zeryd, para, mo, daadir, mado, sol]
    if (update.message.chat.id) == -4058770155 or (authorized_users(user, users)):
        await update.message.reply_text("""
Hello and welcome to the kingdom game bot!
                                    
Here are the main commands:
/start - starts the bot.
/help - shows help.
/result - shows all teams and the amount of health they have.
                                    
And here are more useful commands to know:
Type ' create ' to start creating teams
Type ' stop ' to stop creating teams
Type ' reset ' to remove all the kingdoms
Type ' remove ' to remove a specific team
Type ' atk ' to attack targetes
Type ' def ' to defend against attackers
type ' calc ' to calculate results
type ' end ' to stop all move recording    
"""
)
    if (update.message.chat.type) != "private":
        return False

async def error(update: _update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

def main():

    print("Starting bot...")
    app:Application = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("result", results_command))
    
    app.add_handler(MessageHandler(filters.TEXT,responses))
    

    app.add_handler(MessageHandler(filters.Command, results_command))

    app.add_error_handler(error)

    print("polling...")
    app.run_polling(poll_interval=4)

    print("Bot has stopped")
 

if __name__ == "__main__":
    main()

