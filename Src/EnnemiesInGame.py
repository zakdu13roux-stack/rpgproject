"""
Description:
    Gestion des ennemis en jeu (création, dégâts, soins, accès stats).
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

from Ennemies import Ennemi
from copy import copy

class SetUpEnemy():
    """
    Créer une variable ennemies de self qui est un dictionnaire contenant tout les énnemies (nom, vie, dégats).
    """
    def __init__(self,difficulte=1,nbEnnemi=1, boss=False):
        """
        Description:
            Initialise la liste d'ennemis en jeu.
        Entrées:
            difficulte: niveau de difficulté.
            nbEnnemi: nombre d'ennemis.
            boss: mode boss.
        Sorties:
            Aucune.
        """
        if boss == False:
            self.ennemies = {}
            for i in range(nbEnnemi):
                enemy=Ennemi(difficulte)
                self.ennemies[i]=[enemy.perso[0],enemy.vie,enemy.vie,enemy.attaque]
        else:
            enemy = Ennemi(difficulte, boss)
            self.ennemies={}
            self.ennemies[0]=[enemy.perso[0],enemy.vie,enemy.vie,enemy.attaque]

    def dealDamage(self,enemy,dmg):
        """
        Description:
            Applique des dégâts à un ennemi.
        Entrées:
            enemy: index de l'ennemi.
            dmg: dégâts à appliquer.
        Sorties:
            Aucune.
        """
        if self.ennemies[enemy][2]-dmg<=0:
            self.ennemies[enemy][2]=0
        else:
            self.ennemies[enemy][2]-=dmg
    def Heal(self,enemy,health):
        """
        Description:
            Soigne un ennemi.
        Entrées:
            enemy: index de l'ennemi.
            health: points de soin.
        Sorties:
            Aucune.
        """
        if self.ennemies[enemy][2]+health>=self.ennemies[enemy][1]:
            self.ennemies[enemy][2]=copy(self.ennemies[enemy][1])
        else:
            self.ennemies[enemy][2]+=health

    def GetEnnemieStats(self,enemy):
        """
        Description:
            Retourne les statistiques d'un ennemi.
        Entrées:
            enemy: index de l'ennemi.
        Sorties:
            tuple: statistiques de l'ennemi.
        """
        return self.ennemies[enemy]

    def GetAllEnnemies(self):
        """
        Description:
            Retourne la liste complète des ennemis.
        Entrées:
            Aucune.
        Sorties:
            dict: ennemis en jeu.
        """
        return self.ennemies

    def GetNbEnnemies(self):
        """
        Description:
            Retourne le nombre d'ennemis.
        Entrées:
            Aucune.
        Sorties:
            int: nombre d'ennemis.
        """
        return max(self.ennemies)+1


if __name__ == '__main__':
    test = SetUpEnemy(boss = True)
    print(test.GetEnnemieStats(0))
    test.dealDamage(0,23)
    print(test.GetEnnemieStats(0))
    test.Heal(0,10000)
    print(test.GetEnnemieStats(0))
    print(test.GetAllEnnemies())