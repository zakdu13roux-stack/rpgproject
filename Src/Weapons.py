"""
Description:
    Implémentations des attaques d'armes et application des dégâts.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

from PlayerInGame import *
from EnnemiesInGame import *



def branche(tipe,target,mul):
    """
    Description:
        Applique les dégâts de la branche.
    Entrées:
        tipe: type de cible (joueur ou ennemi).
        target: cible à toucher.
        mul: multiplicateur de dégâts.
    Sorties:
        Aucune.
    """
    if tipe == "player":
        target.takeDamage(10*mul)
    else:
        target.dealDamage(tipe,10*mul)

def H2F(tipe,target,mul):
    """
    Description:
        Applique les dégâts de la hache de fer.
    Entrées:
        tipe: type de cible (joueur ou ennemi).
        target: cible à toucher.
        mul: multiplicateur de dégâts.
    Sorties:
        Aucune.
    """
    if tipe == "player":
        target.takeDamage(32*mul)
    else:
        target.dealDamage(tipe,32*mul)

def epeeRouille(tipe,target,mul):
    """
    Description:
        Applique les dégâts de l'épée rouillée.
    Entrées:
        tipe: type de cible (joueur ou ennemi).
        target: cible à toucher.
        mul: multiplicateur de dégâts.
    Sorties:
        Aucune.
    """
    if tipe == "player":
        target.takeDamage(17*mul)
    else:
        target.dealDamage(tipe,17*mul)

def banane(tipe,target,mul):
    """
    Description:
        Applique les dégâts de la banane.
    Entrées:
        tipe: type de cible (joueur ou ennemi).
        target: cible à toucher.
        mul: multiplicateur de dégâts.
    Sorties:
        Aucune.
    """
    if tipe == "player":
        target.takeDamage(15*mul)
    else:
        target.dealDamage(tipe,15*mul)

def toile(tipe,target,mul):
    """
    Description:
        Applique les dégâts de la toile.
    Entrées:
        tipe: type de cible (joueur ou ennemi).
        target: cible à toucher.
        mul: multiplicateur de dégâts.
    Sorties:
        Aucune.
    """
    if tipe == "player":
        target.takeDamage(11*mul)
    else:
        target.dealDamage(tipe,11*mul)

def lance(tipe,target,mul):
    """
    Description:
        Applique les dégâts de la lance.
    Entrées:
        tipe: type de cible (joueur ou ennemi).
        target: cible à toucher.
        mul: multiplicateur de dégâts.
    Sorties:
        Aucune.
    """
    if tipe == "player":
        target.takeDamage(22*mul)
    else:
        target.dealDamage(tipe,22*mul)