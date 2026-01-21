import arcade

sprite_ref = None
isplayer = None


def Branche(sprite):
    global sprite_ref
    sprite_ref = sprite[2]
    global isplayer
    isplayer = sprite[1]
    arcade.schedule(MoveBranche1, 1/60)


def MoveBranche1(delta_time):
    if isplayer == True:
        sprite_ref.strafe(100)
    else:
        sprite_ref.strafe(-100)
    arcade.unschedule(MoveBranche1)
    arcade.schedule(MoveBranche2, .125)
def MoveBranche2(delta_time):
    arcade.unschedule(MoveBranche2)
    if isplayer == True:
        sprite_ref.strafe(-100)
    else:
        sprite_ref.strafe(100)