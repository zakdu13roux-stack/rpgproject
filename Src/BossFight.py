import arcade
import os
import arcade.gui
import Animations
from EnnemiesInGame import *
from PlayerInGame import *
from PlayerStats import*

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class BossFight(arcade.View):
    def __init__(self, plr,compteur_maps,Cleared_Levels):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

        self.victory = False
        self.victory_timer = 0
        self.compteur_maps = compteur_maps
        self.Cleared_Levels = Cleared_Levels
        self.enemySelected = 0

        # Sprites

        # Sprites décor arrière plan

        self.pelouse={}
        for h in range(2):
            for l in range(3):
                self.pelouse[h*10+l] = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "herbe.webp"), scale =0.5)
                self.pelouse[h*10+l].center_x = 115+235*l
                self.pelouse[h*10+l].center_y = 35+525*h

        self.dirt_path = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "stonepath.png"), scale =1.1)
        self.dirt_path.center_x = 200
        self.dirt_path.center_y = 300

        self.dirt_path2 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "stonepath.png"), scale =1.1)
        self.dirt_path2.center_x = 722
        self.dirt_path2.center_y = 300

        self.trucs_tt_devant_list = arcade.SpriteList()
        self.trucs_tt_devant_list.append(self.dirt_path)
        self.trucs_tt_devant_list.append(self.dirt_path2)
        for p in self.pelouse:
            self.trucs_tt_devant_list.append(self.pelouse[p])

        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "perso.png"), scale=3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 50

        self.Target = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "Target.png"), scale=.7)
        self.Target.center_x = 300
        self.Target.center_y = 500


        self.listeSprite = arcade.SpriteList()
        self.listeSprite.append(self.player_sprite)
        self.listeSprite.append(self.Target)

        self.plr = [plr, self.player_sprite, True]

        self.ViePlayer = arcade.SpriteList()
        self.BarreViePlayer=arcade.SpriteSolidColor(100, 20, arcade.csscolor.GREEN)
        self.BarreViePlayer.center_x = 100
        self.BarreViePlayer.center_y = 20
        self.bordureViePlayer=arcade.SpriteSolidColor(104, 24, arcade.csscolor.GREEN)
        self.bordureViePlayer.center_x = 100
        self.bordureViePlayer.center_y = 20

        self.ViePlayer.append(self.bordureViePlayer)
        self.ViePlayer.append(self.BarreViePlayer)

        self.tour=0

        self.ennemies = {}
        self.nbEnemies = 1
        self.AllEnemy = SetUpEnemy(difficulte=self.compteur_maps, nbEnnemi=self.nbEnemies,boss = True)

        self.healthBars = arcade.SpriteList()
        self.Healths = []
        self.bordureVie=[]

        self.fight_music = arcade.Sound(os.path.join(os.path.dirname(__file__), "..", "Sounds", "musicfight.mp3"), False)
        self.sonjoue = self.fight_music.play(volume=0.2)

        self.batch = arcade.shape_list.ShapeElementList()

        for i in range(self.nbEnemies):
            if self.AllEnemy.GetAllEnnemies()[i][0] == "Snake":
                self.ennemies[i] = [self.AllEnemy.ennemies[i],
                                    arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "snake.png"), scale=0.5),
                                    False]



            self.ennemies[i][1].center_x = 300
            self.ennemies[i][1].center_y = 500
            self.listeSprite.append(self.ennemies[i][1])

            healthBar = arcade.SpriteSolidColor(int((self.ennemies[i][0][2]*100)/self.ennemies[i][0][1]), 20, arcade.csscolor.RED)
            healthBar.center_x = 300
            healthBar.center_y = 400
            self.healthBars.append(healthBar)
            self.Healths.append(self.ennemies[i][0][2])
            self.bordureVie.append(arcade.shape_list.create_rectangle_filled(300,400,104,24, arcade.csscolor.BLACK))
            self.batch.append(self.bordureVie[i])

        # UI manager
        self.manager = arcade.gui.UIManager()

        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=1, vertical_spacing=0, horizontal_spacing=0)

        # Boutons du menu
        resume_button = arcade.gui.UIFlatButton(text="Attack", width=200, height=50)
        self.grid.add(resume_button, col_num=1, row_num=1)
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="right", anchor_y="bottom")

        self.rectangle = arcade.shape_list.ShapeElementList()

        barre1 = arcade.shape_list.create_rectangle_filled(548,570,5,28,arcade.csscolor.BLACK)
        barre2 = arcade.shape_list.create_rectangle_filled(514,585,68,5,arcade.csscolor.BLACK)
        barre3 = arcade.shape_list.create_rectangle_filled(480,570,5,28,arcade.csscolor.BLACK)
        barre4 = arcade.shape_list.create_rectangle_filled(514,555,68,5,arcade.csscolor.BLACK)



        self.rectangle.append(barre1)
        self.rectangle.append(barre2)
        self.rectangle.append(barre3)
        self.rectangle.append(barre4)


        """
        self.abandon_button = arcade.gui.UIFlatButton(text="Abandon", width=200, height=50)
        anchor_abandon = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_abandon.add(child=self.abandon_button, align_x=0, align_y=-275)


        @self.abandon_button.event("on_click")
        def on_click_abandon_button(event):
            from Map import Map
            vuespawn = Map(self.compteur_maps,self.plr[0],self.Cleared_Levels)
            self.window.show_view(vuespawn)
        """

        @resume_button.event("on_click")
        def on_click_resume_button(event):
            self.manager.disable()
            Animations.Attaquer(self.plr, self.AllEnemy, "H2F", self.enemySelected)
            # self.plr,self.AllEnemy,"Branche",0 --> Attaque l'ennemie 0 avec la branche
            # self.ennemies[0],self.plr,"Branche" --> Attaque le joueur avec l'ennemie 0 avec la branche
            self.tour=1
            arcade.schedule(self.SetUpTours, 1/60)


        self.V = arcade.create_text_sprite("Victoire", arcade.csscolor.RED, 50)
        self.V.center_x = 300
        self.V.center_y = 300
        self.text_list = arcade.SpriteList()
        self.text_list.append(self.V)

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.enable()

    def on_hide_view(self):
        self.fight_music.stop(self.sonjoue)
        self.manager.disable()

    def on_update(self, delta_time):
        self.listeSprite.update()

        for i in range(self.nbEnemies):
            self.Healths[i] = self.ennemies[i][0][2]

        if not self.victory and all(h == 0 for h in self.Healths):
            self.victory = True
            self.victory_timer = 0
            self.Target.alpha = 0

        if self.victory:
            self.manager.disable()
            self.victory_timer += delta_time
            if self.victory_timer >= 1:
                from Map import Map
                self.window.show_view(Map(self.plr[0],self.compteur_maps,self.Cleared_Levels))

        if self.plr[0].vie == 0:
            self.manager.disable()
            self.victory_timer += delta_time
            if self.victory_timer >= 1:
                from Spawn import Spawn
                self.window.show_view(Spawn())


        self.Target.angle += 0.2
        if self.Target.scale[0]>.01:
            self.Target.add_scale(-.005)
        else :
            self.Target.alpha = 0


    def on_draw(self):
        self.clear()
        self.trucs_tt_devant_list.draw()
        self.batch.draw()
        self.listeSprite.draw()


        for i in range(self.nbEnemies):
            if self.ennemies[i][0][2] > 0:
                self.healthBars[i].texture = arcade.make_soft_square_texture(20, arcade.csscolor.RED, outer_alpha=255)
                self.healthBars[i].width = int((self.ennemies[i][0][2]*100)/self.ennemies[i][0][1])
            elif self.healthBars[i].alpha != 0:
                self.healthBars[i].alpha = 0
                self.ennemies[i][1].alpha = 0
                die = arcade.load_sound(os.path.join(os.path.dirname(__file__), "..", "Sounds", "Die.wav"))
                die.play(volume=0.2)
                self.batch.remove(self.bordureVie[i])

        self.BarreViePlayer.texture = arcade.make_soft_square_texture(20, arcade.csscolor.GREEN, outer_alpha=255)
        self.BarreViePlayer.width = self.plr[0].GetPlayerStats()[1]*100/self.plr[0].GetPlayerStats()[0]
        self.bordureViePlayer.texture = arcade.make_soft_square_texture(24, arcade.csscolor.BLACK, outer_alpha=255)
        self.bordureViePlayer.width = 104
        self.ViePlayer.draw()
        self.healthBars.draw()

        if self.victory:
            self.text_list.draw()
        elif self.tour == 0:
            self.manager.draw()


    def SetUpTours(self,delta_time):
        self.decalage = 0
        arcade.unschedule(self.SetUpTours)
        arcade.schedule(self.enemyTour, .2)

    def enemyTour(self,delta_time):
        self.EnnemieEnVie = 0
        for vie in self.Healths:
            if vie != 0:
                self.EnnemieEnVie+=1
        if self.tour>self.EnnemieEnVie:
            arcade.unschedule(self.enemyTour)
            self.tour = 0
            self.manager.enable()
        else:
            for i in range(self.nbEnemies):
                if self.Healths[self.tour-1+self.decalage]==0:
                    self.decalage+=1
            if self.Healths[self.tour-1+self.decalage]!=0:
                Animations.Attaquer(self.ennemies[self.tour-1+self.decalage],self.plr,"Branche")
            self.tour+=1


if __name__ == "__main__":
    window = arcade.Window(600, 600, "BossFight")
    BossFight_view = BossFight(player(),1,1)
    window.show_view(BossFight_view)
    arcade.run()