from PlayerInGame import *
from EnnemiesInGame import *



def branche(tipe,target,mul):
    print(tipe,target,mul)
    if tipe == "player":
        target.takeDamage(10*mul)
    else:
        target.dealDamage(tipe,10*mul)