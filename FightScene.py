import arcade
import os
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class FightScene(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT, "FIGHT !!!", False, False)
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

        self.batch = arcade.shape_list.ShapeElementList()
        herbebottom = arcade.shape_list.create_rectangle_filled(0,0,1200,300, arcade.csscolor.GREEN)
        herbetop = arcade.shape_list.create_rectangle_filled(0,SCREEN_HEIGHT,1200,300, arcade.csscolor.GREEN)
        self.batch.append(herbetop)
        self.batch.append(herbebottom)

        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "perso.png"), scale=3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 50

        self.enemy_monkey = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "banana.png"), scale=0.5)
        self.enemy_monkey.center_x = 500
        self.enemy_monkey.center_y = 500



        self.listeSprite = arcade.SpriteList()
        self.listeSprite.append(self.player_sprite)
        self.listeSprite.append(self.enemy_monkey)


    def monterdescend(self, delta_time):
        self.center_y += 10
        time.sleep(0.1)
        self.center_y -= 10



    def on_update(self,delta_time):
        self.listeSprite.update()


    def on_draw(self):
        self.clear()
        self.batch.draw()
        self.listeSprite.draw()




game = FightScene()
arcade.run()