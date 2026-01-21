from PlayerInGame import *
from EnnemiesInGame import *
from Weapons import *

def Start():
    plr = player()
    ennemies = SetUpEnemy()
    enemiesLife = []

    print(plr.Name,"VS",ennemies.GetAllEnnemies())

    for i in range(ennemies.GetNbEnnemies()):
        enemiesLife+=[ennemies.GetEnnemieStats(i)[2]]
    tour=0 #0 -> Joueur  1 -> Ennemies

    while all(vie > 0 for vie in enemiesLife) and plr.vie>0:
        if tour==0:
            branche(0,ennemies,plr.GetPlayerStats()[2])
            enemiesLife[0]=ennemies.GetEnnemieStats(0)[2]
            tour=1
            print("ennemie vie = ",enemiesLife)
        else:
            for i in range(ennemies.GetNbEnnemies()):
                if enemiesLife[i]>0:
                    branche("player",plr,ennemies.GetEnnemieStats(i)[3])
            tour=0
            print(plr.Name,"vie = ",plr.vie,"\n","------------------")
    print("\nFINI\n")
    if plr.vie>0:
        print(plr.Name,"à gagné avec",plr.vie,"pv restant!!")
    else:
        print(ennemies.GetAllEnnemies(),"à gagné avec",enemiesLife,"pv restant!!")


if __name__ == "__main__":
    Start()