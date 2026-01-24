from PlayerInGame import *
from EnnemiesInGame import *



def branche(tipe,target,mul):
    if tipe == "player":
        target.takeDamage(10*mul)
    else:
        target.dealDamage(tipe,10*mul)

def H2F(tipe,target,mul):
    if tipe == "player":
        target.takeDamage(32*mul)
    else:
        target.dealDamage(tipe,32*mul)

def epeeRouille(tipe,target,mul):
    if tipe == "player":
        target.takeDamage(17*mul)
    else:
        target.dealDamage(tipe,17*mul)

def banane(tipe,target,mul):
    if tipe == "player":
        target.takeDamage(15*mul)
    else:
        target.dealDamage(tipe,15*mul)

def toile(tipe,target,mul):
    if tipe == "player":
        target.takeDamage(11*mul)
    else:
        target.dealDamage(tipe,11*mul)