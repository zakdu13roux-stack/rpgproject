import arcade
import Weapons
import os

isPlayer = None
numero = None
sprite_ref = None
userStats = None
Target = None
arme = None


def UseWeapon():
    if isPlayer == True:
        if arme == "Branche":
            Weapons.branche(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == "H2F":
            Weapons.H2F(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == "epeeRouille":
            Weapons.epeeRouille(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == "banane":
            Weapons.banane(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == "toile":
            Weapons.toile(numero,Target,userStats.GetPlayerStats()[2])
    else:
        if arme == "Branche":
            Weapons.branche("player",Target[0],userStats[3])
        elif arme == "H2F":
            Weapons.H2F("player",Target[0],userStats[3])
        elif arme == "epeeRouille":
            Weapons.epeeRouille("player",Target[0],userStats[3])
        elif arme == "banane":
            Weapons.banane("player",Target[0],userStats[3])
        elif arme == "toile":
            Weapons.toile("player",Target[0],userStats[3])

def Attaquer(user,target,weapon,num=0):
    global isPlayer
    isPlayer = user[2]
    global sprite_ref
    sprite_ref = user[1]
    global userStats
    userStats = user[0]
    global numero
    numero = num

    global Target
    Target = target

    global arme
    arme = weapon

    arcade.schedule(Move1, 1/60)


def Move1(delta_time):
    if isPlayer == True:
        scream=arcade.load_sound(os.path.join(os.path.dirname(__file__), "..", "Sounds", "Scream.wav"))
        sprite_ref.strafe(100)
        scream.play(volume=0.2)
        UseWeapon()
    else:
        sprite_ref.strafe(-40)
        UseWeapon()

    arcade.unschedule(Move1)
    arcade.schedule(Move2, .125)

def Move2(delta_time):
    arcade.unschedule(Move2)
    if isPlayer == True:
        sprite_ref.strafe(-100)
    else:
        sprite_ref.strafe(40)
