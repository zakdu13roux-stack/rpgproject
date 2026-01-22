import arcade
import os
import arcade.gui
import Animations
from EnnemiesInGame import *
from PlayerInGame import *

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

        self.listeSprite = arcade.SpriteList()
        self.listeSprite.append(self.player_sprite)

        self.plr = [player(),self.player_sprite,True]


        self.ennemies={}
        self.nbEnemies=3
        self.AllEnemy=SetUpEnemy(nbEnnemi=self.nbEnemies)

        self.healthBars=arcade.SpriteList()

        for i in range(self.nbEnemies):
            if self.AllEnemy.GetAllEnnemies()[i][0]=="Singe":
                self.ennemies[i]=[self.AllEnemy.ennemies[i],arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "banana.png"), scale=0.5),False]
            elif self.AllEnemy.GetAllEnnemies()[i][0]=="Araignee":
                self.ennemies[i]=[self.AllEnemy.ennemies[i],arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "spider.png"), scale=0.06),False]
            elif self.AllEnemy.GetAllEnnemies()[i][0]=="Gorille":
                self.ennemies[i]=[self.AllEnemy.ennemies[i],arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "gorilla.png"), scale=0.4),False]

            self.ennemies[i][1].center_x=500-200*i
            self.ennemies[i][1].center_y=500
            self.listeSprite.append(self.ennemies[i][1])

            healthBar = arcade.SpriteSolidColor(int((self.ennemies[i][0][2]*100)/self.ennemies[i][0][1]), 20, arcade.color.GREEN)
            healthBar.center_x = 500 - 200 * i
            healthBar.center_y = 400
            self.healthBars.append(healthBar)


        # UI manager
        self.manager = arcade.gui.UIManager()

        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=1, vertical_spacing=0, horizontal_spacing=0)

        # Boutons du menu
        resume_button = arcade.gui.UIFlatButton(text="Attack", width=200, height=50)

        # Ajouter les boutons à la grille
        self.grid.add(resume_button, col_num=1, row_num=1)

        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="right", anchor_y="bottom")


        @resume_button.event("on_click")
        def on_click_resume_button(event):
            Animations.Branche(self.plr,self.AllEnemy,"Branche",0) #self.plr,self.AllEnemy,"Branche",0 --> Attaque l'ennemie 0 /// self.ennemies[0],self.plr,"Branche" --> Attaque le joueur avec l'ennemie 0



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
        for i in range(self.nbEnemies):
            if self.ennemies[i][0][2] > 0:
                vieTaille = int((self.ennemies[i][0][2]*100)/self.ennemies[i][0][1])
                self.healthBars[i].texture=arcade.make_soft_square_texture(20, arcade.color.GREEN, outer_alpha=255)
                self.healthBars[i].width=vieTaille
            elif self.healthBars[i].alpha!=0:
                self.healthBars[i].alpha = 0
                self.ennemies[i][1].alpha = 0
                die=arcade.load_sound("Sounds/Die.wav")
                die.play()
        self.healthBars.draw()



if __name__ == "__main__":
    window = arcade.Window(600,600,"FightScene")
    FightScene_view = FightScene()
    window.show_view(FightScene_view)
    arcade.run()