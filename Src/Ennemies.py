"""
Description:
    Définition des ennemis et génération aléatoire selon la difficulté.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

from random import randint, random, choice
from PlayerStats import GetLife, GetAtk
from EnnemiesStats import GetDamageDealers, GetTanks, GetSupports, GetBoss

class Ennemi():
    """ Définit tous les ennemis et leur propriétés dans le jeu:

        - Leur vie basée sur la vie maximum du joueur connecté
        - La force de leur attaque basée sur la vie maximum du joueur conneté
        - Des effets aléatoires qu'ils sont capables d'infliger au joueur.
    """
    def __init__(self,difficulte=1, boss=False):
        """
        Description:
            Initialise un ennemi selon la difficulté et le mode boss.
        Entrées:
            difficulte: niveau de difficulté.
            boss: indique si l'ennemi est un boss.
        Sorties:
            Aucune.
        """
        self.boss = boss
        self.difficulte=difficulte
        self.ennemi_aléatoire()


    def ennemi_aléatoire(self):
        """
        Description:
            Sélectionne un type d'ennemi et calcule ses stats.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        if self.boss == False:
            lst_types = ['Tank', 'Damage Dealer','Support']
            choix_type = choice(lst_types)
        else:
            choix_type = "Boss"
        if choix_type == 'Tank':
            self.vie = 50 + self.difficulte * 10 + randint(40,75)
            temp = round(random(),2)
            while temp > 0.5:
                temp = round(random(),2)
            self.attaque = GetAtk() - temp
            self.Random_Tank()

        elif choix_type == 'Damage Dealer':
            self.vie = 50 + self.difficulte * 10 - randint(20,30)
            temp = round(random(),2)
            while temp > 0.5:
                temp = round(random(),2)
            self.attaque = GetAtk() + temp
            self.Random_Damage_Dealer()

        elif choix_type == 'Support':
            self.vie = 50 + self.difficulte * 10 - randint(25,40)
            temp = round(random(),2)
            while temp > 0.5:
                temp = round(random(),2)
            self.attaque = GetAtk() - temp
            self.Random_Support()

        elif choix_type == 'Boss':
            self.vie = 50 + self.difficulte * 10 + randint(25,40)
            temp = round(random(),2)
            while temp > 0.5:
                temp = round(random(),2)
            self.attaque = GetAtk() + temp
            self.Random_Boss()

    def Random_Damage_Dealer(self):
        """
        Description:
            Récupère un ennemi aléatoire de type DamageDealer.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.perso = choice(GetDamageDealers())

    def Random_Tank(self):
        """
        Description:
            Récupère un ennemi aléatoire de type Tank.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.perso = choice(GetTanks())

    def Random_Support(self):
        """
        Description:
            Récupère un ennemi aléatoire de type Support.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.perso = choice(GetSupports())

    def Random_Boss(self):
        """
        Description:
            Récupère un ennemi aléatoire de type Boss.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.perso = choice(GetBoss())



if __name__ == '__main__':
    Test = Ennemi(boss=True)
    print(Test.perso)
    print((Test.vie,Test.attaque))