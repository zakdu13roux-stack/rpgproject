import arcade
import os
import arcade.gui
import Animations
from EnnemiesInGame import *
from PlayerInGame import *
from Spawn import*
from time import sleep


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class FightScene(arcade.View):
    def __init__(self, compteur_maps):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

        self.victory = False
        self.victory_timer = 0


        self.compteur_maps = compteur_maps

        self.enemySelected=0

        self.batch = arcade.shape_list.ShapeElementList()
        herbebottom = arcade.shape_list.create_rectangle_filled(0,0,1200,300, arcade.csscolor.GREEN)
        herbetop = arcade.shape_list.create_rectangle_filled(0,SCREEN_HEIGHT,1200,300, arcade.csscolor.GREEN)
        self.batch.append(herbetop)
        self.batch.append(herbebottom)

        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "perso.png"), scale=3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 50

        self.Target = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Target.png"), scale=.7)
        self.Target.center_x = 500
        self.Target.center_y = 500

        self.listeSprite = arcade.SpriteList()
        self.listeSprite.append(self.player_sprite)
        self.listeSprite.append(self.Target)

        self.plr = [player(),self.player_sprite,True]


        self.ennemies={}
        self.nbEnemies=3
        self.AllEnemy=SetUpEnemy(difficulte=self.compteur_maps,nbEnnemi=self.nbEnemies)

        self.healthBars=arcade.SpriteList()
        self.Healths=[]

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
            self.Healths.append(self.ennemies[i][0][2])


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


        self.abandon_button = arcade.gui.UIFlatButton(text="Abandon",width=200,height=50)
        anchor_abandon = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_abandon.add(child = self.abandon_button, align_x=0, align_y=-275)

        @self.abandon_button.event("on_click")
        def on_click_abandon_button(event):
            vuespawn = Spawn(self.compteur_maps)
            self.window.show_view(vuespawn)


        @resume_button.event("on_click")
        def on_click_resume_button(event):
            Animations.Branche(self.plr,self.AllEnemy,"Branche",self.enemySelected) #self.plr,self.AllEnemy,"Branche",0 --> Attaque l'ennemie 0 /// self.ennemies[0],self.plr,"Branche" --> Attaque le joueur avec l'ennemie 0
        
        self.V = arcade.create_text_sprite("Victoire", arcade.csscolor.RED, 50)
        self.V.center_x = 300
        self.V.center_y = 300

        self.text_list = arcade.SpriteList()

        self.text_list.append(self.V)



    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_update(self,delta_time):
        self.listeSprite.update()
        for i in range(self.nbEnemies):
            self.Healths[i]=self.ennemies[i][0][2]
        

        if not self.victory and all(h == 0 for h in self.Healths):
            self.victory = True
            self.victory_timer = 0

        if self.victory:
            self.victory_timer += delta_time
            if self.victory_timer >= 1:
                from Map import Map
                self.window.show_view(Map(self.compteur_maps))
        

        if self.Healths[self.enemySelected]==0:
            for i in range(self.nbEnemies):
                if self.Healths[i]!=0 and self.Healths[self.enemySelected]==0:
                    self.enemySelected=i
                    self.Target.center_x = 500-200*i
        self.Target.angle += .2



    def on_draw(self):
        self.clear()
        self.batch.draw()
        self.listeSprite.draw()
        self.manager.draw()
        for i in range(self.nbEnemies):
            if self.ennemies[i][0][2] > 0:
                self.healthBars[i].texture=arcade.make_soft_square_texture(20, arcade.color.GREEN, outer_alpha=255)
                self.healthBars[i].width=int((self.ennemies[i][0][2]*100)/self.ennemies[i][0][1])
            elif self.healthBars[i].alpha!=0:
                self.healthBars[i].alpha = 0
                self.ennemies[i][1].alpha = 0
                die=arcade.load_sound("Sounds/Die.wav")
                die.play()
        self.healthBars.draw()
        if self.Healths[self.enemySelected]==0:
            self.text_list.draw()
            self.Target.alpha = 0

    def on_mouse_press(self,x,y,button,modifier):
        if button == 1:
            if x>410 and x<600 and y>410 and y<600 and self.enemySelected != 0:
                self.enemySelected=0
                self.Target.center_x = 500
            elif x>210 and x<400 and y>410 and y<600 and self.nbEnemies>=2 and self.enemySelected != 1:
                self.enemySelected=1
                self.Target.center_x = 500-200*1
            elif x>0 and x<200 and y>410 and y<600 and self.nbEnemies>=3 and self.enemySelected != 2:
                self.enemySelected=2
                self.Target.center_x = 500-200*2


if __name__ == "__main__":
    window = arcade.Window(600,600,"FightScene")
    FightScene_view = FightScene(1)
    window.show_view(FightScene_view)
    arcade.run()