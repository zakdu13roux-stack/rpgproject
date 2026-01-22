import arcade
import Weapons

isPlayer = None
numero = None
sprite_ref = None
userStats = None
Target = None


def Attaquer(arme):
    if isPlayer == True:
        if arme == "Branche":
            Weapons.branche(numero,Target,userStats.GetPlayerStats()[2])
    else:
        if arme == "Branche":
            Weapons.branche("player",Target[0],userStats[3])

def Branche(user,target,num=0):
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

    arcade.schedule(Move1, 1/60)


def Move1(delta_time):
    if isPlayer == True:
        sprite_ref.strafe(100)
        Attaquer("Branche")
    else:
        sprite_ref.strafe(-100)
        Attaquer("Branche")

    arcade.unschedule(Move1)
    arcade.schedule(Move2, .125)

def Move2(delta_time):
    arcade.unschedule(Move2)
    if isPlayer == True:
        sprite_ref.strafe(-100)
    else:
        sprite_ref.strafe(100)