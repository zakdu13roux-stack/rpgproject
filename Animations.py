import arcade
import time
import FightScene

def Branche(self,sprite):
    self.wait_time = time.monotonic()
    self.waiting = True
    sprite.strafe(200)
    if self.waiting:
            self.wait_time += time.monotonic()
            print(self.wait_time)
            if self.wait_time >= 1:  # 1 second
                print("Done waiting!")
                self.waiting = False
                sprite.strafe(-200)

