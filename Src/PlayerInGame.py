from PlayerStats import GetLife, GetAtk, GetReducDegat, GetName
from copy import copy

class player():
    """
    Créer le joueur et ses stats et donne la possibilité de changer ces stats.
    """
    def __init__(self,sac=[[0 for i in range(3)] for i in range(2)]):
        vie=GetLife()
        self.maxVie = vie
        self.vie = vie
        self.attaque = GetAtk()
        self.ReducDegat = GetReducDegat()
        self.Name = GetName()
        self.sac=sac
        if self.sac==[[0 for i in range(3)] for i in range(2)]:
            self.sac[1][0]=1
            self.sac[0][0]=2

    def takeDamage(self,dmg):
        if self.vie-dmg<=0:
            self.vie=0
        else:
            self.vie-=dmg
    def heal(self,health):
        if self.vie+health>=self.maxVie:
            self.vie=copy(self.maxVie)
        else:
            self.vie+=health

    def GetPlayerStats(self):
        return self.maxVie,self.vie,self.attaque,self.ReducDegat
    
    def GetPlayerWeapons(self):
        return self.sac


if __name__ == '__main__':
    test = player()
    print(test.GetPlayerStats())
    test.takeDamage(67)
    print(test.GetPlayerStats())
    test.heal(1420)
    print(test.GetPlayerStats())