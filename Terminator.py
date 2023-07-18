Terminators = []
Rebels = []
Weapons = []

import random

class Terminator:
    def __init__(self, tag, health, weapon, armor, reflexes):
        self.tag = tag
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.orient = True
        self.nuclear = True
        self.reflexes = reflexes
        Terminators.append(self.tag)

    def __repr__(self):
        return "This {tag} has {health} hit points remaining. They are a Terminator.".format(tag = self.tag, health=self.health)

    def Impersonate(self, Rebel):
        print("It's me, {rebel}.  I'm looking for you but can't find you. Where are you?".format(rebel=Rebel.codename))

    def Reorient(self):
        self.orient = True

    def attack(self, character):
        if self.orient:
            character.health -= self.weapon.damage
            print("{0} attacked {1} using {2}, causing {3} damage. {1}'s remaining health: {4}".format(self.tag, character.codename, self.weapon.name, self.weapon.damage, character.health))
            
        if isinstance(character, Terminator):
           character.orient = False
           print("{0} is disoriented.".format(character.tag))

        else:
            print("{0} is disoriented and must reorient before attacking.".format(self.tag))

class Rebel:
    def __init__(self, codename, health, weapon, armor, reflexes):
        self.codename = codename
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.in_love = True
        self.reflexes = reflexes
        Rebels.append(self.codename)

    def __repr__(self):
        return "This {codename} has {health} hit points remaining. They are a Rebel.".format(codename = self.codename, health=self.health)

    def breather(self):
        self.health += 15

    def attack(self, character):
        character.health -= self.weapon.damage
        print("{0} attacked {1} using {2}, causing {3} damage. {1}'s remaining health: {4}".format(self.codename, character.tag, self.weapon.name, self.weapon.damage, character.health))

        if isinstance(character, Terminator):
            character.orient = False
            print("{0} is disoriented.".format(character.tag))

    def ambush(self, terminator):
        self.attack(terminator)
        self.attack(terminator)         


class Weapon:
    def __init__(self, name, sort, damage):
        self.name = name
        self.sort = sort
        self.damage = damage     
        Weapons.append(self.name)

    def __repr__(self):
        return "This {name} can cause {damage} points of damage. It is a weapon.".format(name = self.name, damage=self.damage)

Machete = Weapon("Machete", "Edged", 15)
Shotgun = Weapon("Sawed Off Shotgun", "Gun", 27)
Uzi = Weapon("Uzi", "Gun", 42)
Reese = Rebel("Reese", 87, Shotgun, "light", 92)
Sarah_Connors = Rebel("Sarah", 63, Machete, "Light", 68)
T1000 = Terminator("T1000", 350, Uzi, "Heavy", 45)
T2000 = Terminator("T2000", 225, "Blades", "Extreme", 67)

players = [Reese, T1000]

while players[0].health > 0 and players[1].health > 0:
    random.shuffle(players)  # shuffle players before each round
    for player in sorted(players, key=lambda p: p.reflexes + random.randint(1, 100), reverse=True):
        if player.health > 0:
            if isinstance(player, Rebel):
                player.attack(T1000)  # the Rebel always attacks the Terminator
            elif isinstance(player, Terminator):
                if player.orient:
                    player.attack(Reese)  # the Terminator always attacks the Rebel
                else:
                    player.Reorient()  # if disoriented, the Terminator must Reorient


#print(Rebels)
#print(Terminators)
#print(Weapons)

#T1000.Impersonate(Reese)
#Reese.attack(T1000) # Reese attacks T1000
#T1000.attack(Reese) # T1000 attacks Reese
#clearReese.attack(T1000) # Reese attacks T1000