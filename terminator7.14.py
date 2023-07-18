
Terminators = []
Rebels = []
Weapons = []

import random
import time
from colorama import Fore, Style
import keyboard

def slow_print(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.05)
    print()

class Terminator:
    def __init__(self, tag, health, weapon, armor, reflexes, to_hit=None, evade=None):
        self.tag = tag
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.orient = True
        self.nuclear = True
        self.reflexes = reflexes
        self.to_hit = to_hit if to_hit is not None else random.randint(1, 100)  # Set to_hit
        self.evade = evade if evade is not None else random.randint(1, 25)
        Terminators.append(self)

    def __repr__(self):
        return "This {tag} has {health} hit points remaining. They are a Terminator.".format(tag = self.tag, health=self.health)

    def impersonate(self, Rebel):
        time.sleep(1) 
        slow_print("It's me, {rebel}. I'm looking for you but can't find you. Where are you?".format(rebel=Rebel.codename))
    
    def take_turn(self, target, action=None):
        action = input("{0}, it's your turn! Type 'ATT' to attack or 'RESET' to reorient: ".format(self.tag)).upper()
        if self.orient:
            if action.upper() == 'ATT':
                self.attack(target)
            elif action.upper() == 'IMP':
                self.impersonate()
            else:
                slow_print(Fore.RED + "Invalid action! Type ATT to attack or IMP to impersonate your opponents voice." + Style.RESET_ALL)
        else:
            slow_print(Fore.GREEN + "Your system is disoriented and rebooting now." + Style.RESET_ALL)
            self.Reorient()    
            return       

    def Reorient(self):
        self.orient = True
        time.sleep(1) 
        slow_print("SQUAWK System Reorienting...")

    def attack(self, character):  
        hit_roll = random.randint(1, 100)
        required_roll = max((self.to_hit + self.weapon.accuracy_bonus) - (character.evade if character.evade else 0), 1)

        if hit_roll <= 5:
            slow_print(Fore.BLUE + "{0} attacks with their {1} and misses.".format(self.tag, self.weapon.name) + Style.RESET_ALL)

        elif hit_roll >= 96:
            damage_dealt = self.weapon.damage * 2
            damage_dealt -= (damage_dealt * (character.armor.percent_absorption / 100))
            character.health -= damage_dealt
            slow_print(Fore.RED + "{0} landed a CRITICAL HIT on {1} using {2}, causing {3} damage. {1}'s remaining health: {4}".format(
                self.tag,
                character.codename if isinstance(character, Rebel) else character.tag,
                self.weapon.name,
                damage_dealt,
                character.health) + Style.RESET_ALL)

        elif hit_roll > required_roll:
            slow_print(Fore.BLUE + "{0} attacks with their {1} and misses.".format(self.tag, self.weapon.name) + Style.RESET_ALL)

        else:
            if self.orient:
                    damage_dealt = self.weapon.damage 
                    damage_dealt -= (damage_dealt * (character.armor.percent_absorption / 100))
                    character.health -= damage_dealt                
                    slow_print(Fore.RED + "{0} attacked {1} using {2}, causing {3} damage. {1}'s remaining health: {4}".format(
                        self.tag,
                        character.codename if isinstance(character, Rebel) else character.tag,
                        self.weapon.name,
                        damage_dealt,   
                        character.health) + Style.RESET_ALL)
                    
                    if isinstance(character, Terminator):
                        character.orient = False
                        slow_print(Fore.GREEN + "{0} is disoriented.".format(character.tag) + Style.RESET_ALL)

                    if isinstance(character, Rebel):
                        bleed_roll = random.randint(1, 100)
                        if bleed_roll <= 33:
                            character.bleed = True
                            slow_print(Fore.GREEN + "That attack has caused {0} to be seriously bleeding!".format(character.codename) + Style.RESET_ALL)

            else:
                slow_print(Fore.GREEN + "{0} is disoriented and must reorient before attacking.".format(self.tag) + Style.RESET_ALL)

class Rebel:
    def __init__(self, codename, health, weapon, armor, reflexes, to_hit=None, evade=None):
        self.codename = codename
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.in_love = True
        self.reflexes = reflexes
        self.to_hit = to_hit if to_hit is not None else random.randint(1, 100)  # Set to_hit
        self.evade = evade if evade is not None else random.randint(1, 25)
        self.bleed = False
        Rebels.append(self)

    def __repr__(self):
        return "This {codename} has {health} hit points remaining. They are a Rebel.".format(codename = self.codename, health=self.health)
   
    def take_turn(self, target, action):
        action = input("{0}, it's your turn! Type 'ATT' to attack or 'MED' to heal: ".format(self.codename)).upper()
        if action.upper() == 'ATT':
            self.attack(target)
        elif action.upper() == 'MED':
            self.breather()
        else:
            slow_print(Fore.RED + "Invalid action! Type ATT to attack or MED to hheal/stop bleeding" + Style.RESET_ALL)

    def breather(self):
        self.health += 25
        self.bleed = False

    def attack(self, character):  
        hit_roll = random.randint(1, 100)
        required_roll = max((self.to_hit + self.weapon.accuracy_bonus) - (character.evade if character.evade else 0), 1)
        if hit_roll <= 5:
            slow_print(Fore.BLUE + "{0} attacks with their {1} and misses.".format(self.codename, self.weapon.name) + Style.RESET_ALL)
        elif hit_roll >= 96:
            damage_dealt = self.weapon.damage * 2
            damage_dealt -= (damage_dealt * (character.armor.percent_absorption / 100))
            character.health -= damage_dealt
            slow_print(Fore.RED + "{0} landed a CRITICAL HIT on {1} using {2}, causing {3} damage. {1}'s remaining health: {4}".format(
                self.codename,
                character.tag if isinstance(character, Terminator) else character.codename,
                self.weapon.name,
                damage_dealt,
                character.health) + Style.RESET_ALL)
            if isinstance(character, Terminator):
                character.orient = False
                slow_print("{0} is disoriented.".format(character.tag))
        elif hit_roll > required_roll:
            slow_print(Fore.BLUE + "{0} attacks with their {1} and misses.".format(self.codename, self.weapon.name) + Style.RESET_ALL)
        else:
            damage_dealt = self.weapon.damage 
            damage_dealt -= (damage_dealt * (character.armor.percent_absorption / 100))
            character.health -= damage_dealt            
            slow_print(Fore.RED + "{0} attacked {1} using {2}, causing {3} damage. {1}'s remaining health: {4}".format(
                self.codename,
                character.tag if isinstance(character, Terminator) else character.codename,
                self.weapon.name,
                damage_dealt,
                character.health) + Style.RESET_ALL)
            if isinstance(character, Terminator):
                character.orient = False
                slow_print(Fore.GREEN + "{0} is disoriented.".format(character.tag) + Style.RESET_ALL)

    def ambush(self, terminator):
        self.attack(terminator)
        self.attack(terminator)

class Weapon:
    def __init__(self, name, sort, damage, accuracy_bonus=0):
        self.name = name
        self.sort = sort
        self.damage = damage
        self.accuracy_bonus = accuracy_bonus
        Weapons.append(self.name)

    def __repr__(self):
        return "This {name} can cause {damage} points of damage. It is a weapon.".format(name = self.name, damage=self.damage)

class Armor:
    def __init__(self, strength, percent_absorption):
        self.strength = strength
        self.percent_absorption = percent_absorption


#Weapons
Machete = Weapon("Machete", "Edged", 15, 5)
Blades = Weapon("Blades", "Edged", 35, 0)
Shotgun = Weapon("Sawed Off Shotgun", "Gun", 27, 20)
Uzi = Weapon("Uzi", "Gun", 42, -12)
Automatic_Pistol = Weapon("Colt Chambered Pistol", "Gun", 20, 0)
AK47 = Weapon("AK47", "Gun", 55, -10)
Gatling = Weapon("Gatling Gun", "Gun", 92, -20)
Grenade_Launcher = Weapon("Grenade Launcher", "Gun", 72, 0)
Longslide = Weapon(".45 longslide with laser sighting", "Gun", 20, 35)
Twelve_Gauge = Weapon("12 Gauge Auto-Loader", "Gun", 37, 45)

#Armor
Light = Armor("Light", 5)
Medium = Armor("Medium", 30)
Heavy = Armor("Heavy", 50)
Extreme = Armor("Extreme", 75)  

#Rebels
Sarah = Rebel('Sarah Connors', 78, Machete, Light, 81, 48)
John_Young = Rebel('Young John Connors', 58, Automatic_Pistol, Light, 26, 44)
Reese = Rebel("Reese", 87, Shotgun, Light, 92, 50)
Enrique = Rebel('Enrique Salceda', 61, AK47, Medium, 55, 29)

#Terminators
T800 = Terminator("T-800", 350, Longslide, Heavy, 45, 10)
T1000 = Terminator("T-1000", 225, Blades, Extreme, 64, 32)
T3000 = Terminator("T-3000", 540, Machete, Heavy, 100, 100)

def yes_or_no(question):
    while True:
        answer = input(question + " (yes/no): ").lower().strip()
        if answer in ['yes', 'no']:
            return answer == 'yes'

def yes_or_no(question):
    while True:
        answer = input(question + " (yes/no): ").lower().strip()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        else:
            time.sleep(1) 
            slow_print("Please answer 'yes' or 'no'.")

def choose_option(question, option1, option2):
    while True:
        answer = input(question + " ({0}/{1}): ".format(option1, option2)).lower().strip()
        if answer in [option1, option2]:
            return answer
        else:
            time.sleep(1) 
            slow_print("Please answer '{0}' or '{1}'.".format(option1, option2))

def choose_character(character_type):
    while True:
        characters = Rebels if character_type == 'Rebel' else Terminators
        for i, character in enumerate(characters):
            slow_print("{0}. {1}".format(i+1, character.codename if isinstance(character, Rebel) else character.tag))
        choice = input("Choose your {0} (enter the number): ".format(character_type))
        if choice.isdigit() and 1 <= int(choice) <= len(characters):
            return characters[int(choice)-1]
        else:
            slow_print("Invalid choice. Please choose a number from the list.")

print("Welcome, User.")
if yes_or_no("Would you like to play a game of TERMINATOR DEATH MATCH?"):
    character_type = choose_option("Would you prefer to play as a rebel or as a terminator?", "rebel", "terminator").title()
    user_character = choose_character(character_type)
    time.sleep(1) 
    slow_print("You are playing as {0}.\n".format(user_character.codename if isinstance(user_character, Rebel) else user_character.tag))

    # Get the list of characters from the opposing side opposing_characters = Terminators if isinstance(user_character, Rebel) else Rebels
    opposing_characters = Terminators if isinstance(user_character, Rebel) else Rebels

    # Choose a random character from the opposing side
    random_opponent = random.choice(opposing_characters)

    # Set the players list
    players = [user_character, random_opponent]

    while players[0].health > 0 and players[1].health > 0:
        print(" ")
        print(" ")
        print("NEW ROUND")

        for p in players:
            if isinstance(p, Rebel) and p.bleed:
                bleed_damage = 5
                p.health -= bleed_damage
                slow_print(Fore.GREEN + "{0} is bleeding, causing 5 points of damage and reducing their health to {1}.".format(p.codename, p.health) + Style.RESET_ALL)
        
        for p in players:
            if isinstance(p, Terminator) and p.orient == False:
                slow_print(Fore.GREEN + "{0} is disoriented and needs to reorient.".format(p.tag) +Style.RESET_ALL)

        time.sleep(1)
        input("\nPress enter to continue with the next reflex roll...")
        # Determine the order of turns for this round
        random.shuffle(players)
        reflex_scores = [(p, p.reflexes + random.randint(1, 100)) for p in players]
        reflex_scores.sort(key=lambda x: x[1], reverse=True)
        first_player, second_player = reflex_scores[0][0], reflex_scores[1][0]

        #reflex roll results
        time.sleep(1)  
        slow_print("{0} rolled {1} + {2} (reflexes) = {3}".format(first_player.codename if isinstance(first_player, Rebel) else first_player.tag, reflex_scores[0][1] - first_player.reflexes, first_player.reflexes, reflex_scores[0][1]))
        time.sleep(1)  
        slow_print("{0} rolled {1} + {2} (reflexes) = {3}".format(second_player.codename if isinstance(second_player, Rebel) else second_player.tag, reflex_scores[1][1] - second_player.reflexes, second_player.reflexes, reflex_scores[1][1]))
        time.sleep(1)  
        slow_print("{0} wins the roll and goes first!\n".format(first_player.codename if isinstance(first_player, Rebel) else first_player.tag))
    
        #player turns
        if isinstance(first_player, Rebel):
            first_player.take_turn(second_player, action)
        else:  # It's a Terminator's turn
            first_player.take_turn(second_player, action)
    
        if second_player.health > 0: 
            if isinstance(second_player, Rebel):
                second_player.take_turn(first_player, action)
            else:  # It's a Terminator's turn
                second_player.take_turn(first_player, action)
 
else:
    time.sleep(4) 
    slow_print(" ")
    slow_print("Chicken.")
    slow_print(" ")
    