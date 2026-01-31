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
        self.boss = boss
        self.difficulte=difficulte
        self.ennemi_aléatoire()


    def ennemi_aléatoire(self):
        """
        Choisis un type aléatoire parmis les 3 existants :
            - Tank
            - Damage Dealer
            - Support

        Sortie : - Les PV de l'ennemi (INT)
                 - Les multiplicateur des dégats de l'ennemi
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
        """Récupère un ennemi aléatoire de la catégorie "DamageDealer"
         dans la table "enemies" de la base de données """
        self.perso = choice(GetDamageDealers())

    def Random_Tank(self):
        """Récupère un ennemi aléatoire de la catégorie ""
         dans la table "enemies" de la base de données """
        self.perso = choice(GetTanks())

    def Random_Support(self):
        """Récupère un ennemi aléatoire de la catégorie "Support"
         dans la table "enemies" de la base de données """
        self.perso = choice(GetSupports())

    def Random_Boss(self):
        """Récupère un ennemi aléatoire de la catégorie "Boss"
         dans la table "enemies" de la base de données """
        self.perso = choice(GetBoss())



if __name__ == '__main__':
    Test = Ennemi(boss=True)
    print(Test.perso)
    print((Test.vie,Test.attaque))