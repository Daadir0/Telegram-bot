from telegram import _update
from telegram.ext import ContextTypes
from authorization import *


def Leader_m(update: _update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.chat.id

    if authorized_users(user):
        pass

def setleader (text, setting):
    while setting:
        if "." == text:
            setting = False
            if len(leaders) > 0:
                result = ""
                for l,t in leaders.items():
                    result += f"{l} is the leader of [{t}].\n"
                return f"setting leaders have ended\n\n{result}"
            else:
                return "setting leaders have ended"
        words = text.split()
        for word in words:
            if word in kingdoms:
                team = word
            elif word not in leaders and (word not in kingdoms):
                leader = word
            else:
                return "unclear, please try again latter"
        leaders[leader] = team
        return (f"{leader} is the leader of {team}")