import arcade
import time
import FightScene

def Branche(sprite):
    print("Go")
    MoveBranche1(sprite)

def MoveBranche1(sprite):
    sprite.strafe(200)
    arcade.schedule(MoveBranche2(sprite), 1)
def MoveBranche2(sprite):
    arcade.unschedule(MoveBranche2)
    sprite.strafe(-200)
    print("Done waiting!")