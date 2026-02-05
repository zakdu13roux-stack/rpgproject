"""
Description:
    Classe joueur en jeu et gestion de ses statistiques et inventaire.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

from PlayerStats import GetLife, GetAtk, GetReducDegat, GetName, GetItems
from copy import copy

class player():
    """
    Créer le joueur et ses stats et donne la possibilité de changer ces stats.
    """
    def __init__(self):
        """
        Description:
            Initialise le joueur et son inventaire.
        Entrées:
            sac: matrice d'objets du sac.
        Sorties:
            Aucune.
        """
        vie=GetLife()
        self.maxVie = vie
        self.vie = vie
        self.attaque = GetAtk()
        self.ReducDegat = GetReducDegat()
        self.Name = GetName()
        self.sac=GetItems()
        if self.sac==[[0 for i in range(3)] for i in range(2)]:
            self.sac[1][0]=1
            self.sac[0][0]=2

    def takeDamage(self,dmg):
        """
        Description:
            Applique des dégâts au joueur.
        Entrées:
            dmg: dégâts à appliquer.
        Sorties:
            Aucune.
        """
        if self.vie-dmg<=0:
            self.vie=0
        else:
            self.vie-=dmg
    def heal(self,health):
        """
        Description:
            Soigne le joueur.
        Entrées:
            health: points de soin.
        Sorties:
            Aucune.
        """
        if self.vie+health>=self.maxVie:
            self.vie=copy(self.maxVie)
        else:
            self.vie+=health

    def GetPlayerStats(self):
        """
        Description:
            Retourne les statistiques du joueur.
        Entrées:
            Aucune.
        Sorties:
            tuple: statistiques du joueur.
        """
        return self.maxVie,self.vie,self.attaque,self.ReducDegat

    def GetPlayerWeapons(self):
        """
        Description:
            Retourne l'inventaire d'armes du joueur.
        Entrées:
            Aucune.
        Sorties:
            list: sac du joueur.
        """
        return self.sac


if __name__ == '__main__':
    test = player()
    print(test.GetPlayerStats())
    test.takeDamage(67)
    print(test.GetPlayerStats())
    test.heal(1420)
    print(test.GetPlayerStats())