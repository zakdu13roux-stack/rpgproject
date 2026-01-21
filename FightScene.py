import arcade
import os
import arcade.gui
import Animations

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class FightScene(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

        self.batch = arcade.shape_list.ShapeElementList()
        herbebottom = arcade.shape_list.create_rectangle_filled(0,0,1200,300, arcade.csscolor.GREEN)
        herbetop = arcade.shape_list.create_rectangle_filled(0,SCREEN_HEIGHT,1200,300, arcade.csscolor.GREEN)
        self.batch.append(herbetop)
        self.batch.append(herbebottom)

        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "perso.png"), scale=3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 50
        self.player_sprite.Player = True

        self.enemy_monkey = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "banana.png"), scale=0.5)
        self.enemy_monkey.center_x = 500
        self.enemy_monkey.center_y = 500
        self.enemy_monkey.Player = False

        self.listeSprite = arcade.SpriteList()
        self.listeSprite.append(self.player_sprite)
        self.listeSprite.append(self.enemy_monkey)


        # UI manager
        self.manager = arcade.gui.UIManager()

        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=1, vertical_spacing=0, horizontal_spacing=0)

        # Boutons du menu
        resume_button = arcade.gui.UIFlatButton(text="Resume", width=200, height=50)

        # Ajouter les boutons à la grille

        self.grid.add(resume_button, col_num=1, row_num=1)

        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="center", anchor_y="center")


        @resume_button.event("on_click")
        def on_click_resume_button(event):
            Animations.Branche(self.enemy_monkey)



    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_update(self,delta_time):
        self.listeSprite.update()


    def on_draw(self):
        self.clear()
        self.batch.draw()
        self.listeSprite.draw()
        self.manager.draw()



if __name__ == "__main__":
    window = arcade.Window(600,600,"FightScene")
    FightScene_view = FightScene()
    window.show_view(FightScene_view)
    arcade.run()