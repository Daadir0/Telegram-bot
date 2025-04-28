from authorization import kingdoms

attacker = {}
defender = {}

kingdom_name = ()

def attacking_phase(text):
    global attacker, kingdom_name 

    if text in kingdoms:
        if text in attacker:
            kingdom_name = text
            return f"{text} is ready to attack again"
        if text != kingdom_name:
            attacker[text] = []
            kingdom_name = text
            return f"Who is {text} attacking?"
    else:
        return ("This kingdom does not exist, please try again.")

def target_selection_phase(text):
    global attacker, kingdom_name
    targets = []
    if "all" in text:
        for name in kingdoms:
            if name == kingdom_name:
                continue
            else:
                targets.append(name)
    if text in kingdoms:
        if text == kingdom_name:
            return("You can't attack yourself.")
        elif text in attacker.get(kingdom_name):
            return ("You can't attack the same target twice.")
        else:
            targets.append(text)
    words = text.split()
    for word in words:
        if word in kingdoms:
            if word == kingdom_name:
                return("You can't attack yourself.")
            elif word in attacker.get(kingdom_name):
                return ("You can't attack the same target twice.")
            else:
                targets.append(word)
        else:
            return (f"'{word}' is not a kingdom, please try again.")
        
    if kingdom_name in attacker: # If the same attacker is attacking again, merge the targets
        attacker[kingdom_name] += targets
        attacker[kingdom_name] = list(set(attacker[kingdom_name]))  # Remove duplicate targets
        current_target = attacker.get(kingdom_name)
        return(f"{kingdom_name} Currently targeting: \n{current_target}")
    else:
        return (f"'{word}' is not a kingdom, please try again.")

def defending_phase():
    global defender,kingdom_name

    if kingdom_name in kingdoms:
        defender[kingdom_name] = []
        return f"Who is {kingdom_name} defending against?"
    else:
        return ("This kingdom does not exist, please try again.")

def defend_selection_phase(text):
    global defender,kingdom_name
    defended_from = []
    if "all" in text:
        for name in kingdoms:
            if name == kingdom_name:
                continue
            else:
                defended_from.append(name)

    if text in kingdoms:
        if text == kingdom_name:
            return ("You can't defend from yourself.")
        elif text in defender.get(kingdom_name):
            return ("You can't defend against the same kingdom twice.")
        else:
            defended_from.append(text)
    words = text.split()
    for word in words:
        if word in kingdoms:
            if word == kingdom_name:
                return ("You can't defend from yourself.")
            elif word in defender.get(kingdom_name):
                return ("You can't defend against the same kingdom twice.")
            else:
                defended_from.append(word)
        else:
            return (f"'{word}' is not a kingdom, please try again.")
    if kingdom_name in defender:
        defender[kingdom_name] += defended_from
        defender[kingdom_name] = list(set(defender[kingdom_name]))
        current_defended = defender.get(kingdom_name)
        return(f"{kingdom_name} Currently defending agaisnt: \n{current_defended}")
    else:
        return (f"'{word}' is not a kingdom, please try again.")
    
"""     defender[kingdom_name] = defended_from
        current_defended = defender.get(kingdom_name)
        return(f"{kingdom_name} Currently defending agaisnt: \n{current_defended}")"""

def calculating_phase():
    global kingdoms, defender, attacker


    for defender_team, defended_from in defender.items(): #so it seprates defender into two first "defender_team" which is the ones that defending and second "defended_from" which are the attackers 
        if defender_team in kingdoms:
            kingdoms[defender_team] -= len(defended_from)

    for attacker_team, target_list in attacker.items():
        if attacker_team in kingdoms:
            kingdoms[attacker_team] -= len(target_list)  # Lose 1 point for each target

    for attacker_team, target_list in attacker.items():
        for target_kingdom in target_list:
            if target_kingdom in defender:
                if attacker_team in defender.get(target_kingdom):
                    continue
            kingdoms[target_kingdom] -= 3
        
        
    result_attacks = "\n".join([f"{attacker_team} = {', '.join(target_list)}" for attacker_team, target_list in attacker.items()])
    result_defends = "\n".join([f"{defender_team} = {', '.join(defended_from)}" for defender_team, defended_from in defender.items()])
    no_attack = "\n".join([f"{name} = " for name in kingdoms if name not in attacker])
    no_defend = "\n".join([f"{name} = " for name in kingdoms if name not in defender])
    sort_kingdoms = dict(sorted(kingdoms.items(), key=lambda item: item[1], reverse=True))
    result = "\n".join([f"{t.capitalize()} = {h}" for t, h in sort_kingdoms.items()])
    attacker.clear()
    defender.clear()
    return (f" Attcks:\n{result_attacks}\n{no_attack}\n\nDefend:\n{result_defends}\n{no_defend}\n\nResults:\n{result}")

    
    



# Main game loop

