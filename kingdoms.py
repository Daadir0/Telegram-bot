from telegram import _update
from telegram.ext import ContextTypes
from handles_moves import *
from authorization import *

creating = False
defending = False
targeting = False
calculating = False
defendee = False

def messages(text: str):
    text: str = text.lower().strip()
    global creating, targeting, defending, calculating, defendee
    if text in kingdoms:
        if (targeting == False) and defendee == False:
            attack = attacking_phase(text)
            if attack == (f"Who is {text} attacking?" or f"{text} is ready to attack again"):
                targeting = True
                return attack
        else:
            pass
    elif "create" == text:
        creating = True
        return "You've started the kingdom creation process, starting from now on every message you send is counted as a seprate kingdom\n\nTo stop the kingdom creation process type 'stop'\n\nTo remove all teams and restart the process type'reset'\n\nTo remove a specific kingdom type 'remove' + the kingdom's name."
    elif "remove" in text:
        new_text = text.replace("remove", "").strip()
        if new_text in kingdoms:
            kingdoms.pop(new_text)
            return f"{new_text} have been removed from kingdoms\n"
        elif "remove" == text:
            return "Add the name of the kingdom in the message\n\nFor example:\nremove kindom 1"
        else:
            return "This kingdom does not exist"
    elif "stop" == text:
        creating = False
        amout = len(kingdoms)
        return f"There are {amout} kingdoms already!, if you want to see all the kingdoms you have created so far just press here. --->'/result'"
    elif 'reset' == text:
        creating = False
        kingdoms.clear()
        attacker.clear()
        defender.clear()
        return "all kingdoms have been removed.\n\ntype 'create' to creat new kingdoms"
    elif "calc" == text:
        calculating = True
        defending = False
        targeting = False
        defendee = False
    elif "end" == text:
        creating = False
        defending = False
        targeting = False
        calculating = False
        defendee = False
        return "everything the bot was doing have stopped if you wish to do something press her and learn what you can do '/help'"
    elif "cancel" in text:
        attacker.clear()
        defender.clear()
        calculating = True

    while creating:
        words = text.split()
        name = ' '.join(words[:-1])  # Join all words except the last one to get the kingdom name
        hp = words[-1]

        if name in kingdoms:
            return f"{name} already exists"
        else:
            if not name.replace(" ", "").isalpha():  # Check if the name contains only letters
                return f"({name}) is Invalid! The name of the kingdom should only contain letters."

            if not hp.isdigit():  # Check if health contains only numbers
                return f"({hp}) is Invalid! The health of the kingdom should only contain numbers."

            kingdoms[name] = int(hp)
            return "Kingdom is created successfully!"

    while targeting:
        if text == ".":
            targeting = False
            defending = True
            break
        target = target_selection_phase(text)
        if target == "You can't attack yourself.":
            return target
        elif target == "You can't attack the same target twice.":
            return target
        elif target == "This kingdom does not exist, please try again.":
            return target
        else:
            return target
    
    while defending:
        defend = defending_phase()
        if defend == "This kingdom does not exist, please try again.":
            return defend
        else:
            defending = False
            defendee = True
            return defend
    
    while defendee:
        if text == ".":
            defendee = False
            return "ok you can move on to the next kingdom"
        defended = defend_selection_phase(text)
        if defended == "You can't defend from yourself.":
            return defended
        elif defended == "You can't defend from the same person twice.":
            return defended
        elif defended == "This kingdom does not exist, please try again.":
            return defended
        else:
            return defended
    
    while calculating:
        calculate = calculating_phase()
        calculating = False
        return calculate 
              
    else:
        return "I dont understand..."


