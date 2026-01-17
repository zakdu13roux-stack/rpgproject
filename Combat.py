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

    while all(vie != 0 for vie in enemiesLife) and plr.vie>0:
        if tour==0:
            branche(0,ennemies,plr.GetPlayerStats()[2])
            tour=1
        else:
            for i in range(ennemies.GetNbEnnemies()):
                if enemiesLife[i]>0:
                    print(ennemies.GetEnnemieStats(i)[3])
                    branche("player",plr,ennemies.GetEnnemieStats(i)[3])
            tour=0
        print("plr vie = ",plr.vie)
        print("ennemie vie = ",enemiesLife)



Start()