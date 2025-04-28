from telegram import _update
from telegram.ext import ContextTypes
from kingdoms import messages
from authorization import *

BOT_NAME = 'Kobe_kingdom_bot'
response: str = ()
async def responses(update: _update, context: ContextTypes.DEFAULT_TYPE):
    global response
    message_type:str = update.message.chat.type
    text:str = update.message.text
    user = update.message.chat.id
    users = [zeryd, para, mo, daadir, mado, sol,aabe]

    print(f'({update.message.chat.id}) {update.message.chat.first_name} said in {message_type}:"{text}"')
    
    if message_type == "private":
        if authorized_users(user, users) :
            response = messages(text)
            await update.message.reply_text(response)
            print("Bot:", response)
        else:
            await update.message.reply_text("You are not an Authorized user")
            print ("Bot: You are not an Authorized user")
    else:
        return False
    
async def results_command(update: _update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.chat.id
    users = [zeryd, para, mo, daadir, mado, sol]
    if (update.message.chat.id) == -4058770155 or (authorized_users(user, users)):
        if len(kingdoms) >= 2:
            result = ""
            sort_kingdoms = dict(sorted(kingdoms.items(), key=lambda item: item[1], reverse=True))
            for t, h in sort_kingdoms.items():
                result += f"{t.capitalize()} = {h}\n"
            await update.message.reply_text(f"these are the teams and their health:\n\n{result}")
        else:
            await update.message.reply_text(f"you did not create enough teams.")
            await update.message.reply_text("try adding more teams!\n\nTo add more teams type 'start'\n\nto remove all teams type 'reset' then go back to the first step\n\nif you've created enough teams type 'stop' ")

