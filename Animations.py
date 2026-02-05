"""
Description:
    Gère les animations d'attaque et l'exécution des armes.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

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
    """
    Description:
        Exécute l'attaque correspondant à l'arme sélectionnée.
    Entrées:
        Aucune.
    Sorties:
        Aucune.
    """
    if isPlayer == True:
        if arme == 1:#Branche
            Weapons.branche(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == 2:#Banane
            Weapons.banane(numero,Target,userStats.GetPlayerStats()[2],userStats)
        elif arme == 3:#Hache de Fer
            Weapons.H2F(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == 4:#Epée rouillée
            Weapons.epeeRouille(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == 5:#Lance
            Weapons.lance(numero,Target,userStats.GetPlayerStats()[2])
        elif arme == "toile":
            Weapons.toile(numero,Target,userStats.GetPlayerStats()[2])
    else:
        if arme == 1: #Branche
            Weapons.branche("player",Target[0],userStats[3])
        elif arme == 2: #Banane
            Weapons.banane("player",Target[0],userStats[3])
        elif arme == 3: #Hache de Fer
            Weapons.H2F("player",Target[0],userStats[3])
        elif arme == 4: #Epée rouillée
            Weapons.epeeRouille("player",Target[0],userStats[3])
        elif arme == 5: #Lance
            Weapons.lance("player",Target[0],userStats[3])
        elif arme == "toile":
            Weapons.toile("player",Target[0],userStats[3])

def Attaquer(user,target,weapon,num=0):
    """
    Description:
        Initialise l'attaque et planifie l'animation.
    Entrées:
        user: données du lanceur d'attaque.
        target: cible de l'attaque.
        weapon: arme utilisée.
        num: index de la cible.
    Sorties:
        Aucune.
    """
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
    """
    Description:
        Première phase d'animation d'attaque.
    Entrées:
        delta_time: pas de temps.
    Sorties:
        Aucune.
    """
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
    """
    Description:
        Deuxième phase d'animation d'attaque.
    Entrées:
        delta_time: pas de temps.
    Sorties:
        Aucune.
    """
    arcade.unschedule(Move2)
    if isPlayer == True:
        sprite_ref.strafe(-100)
    else:
        sprite_ref.strafe(40)
