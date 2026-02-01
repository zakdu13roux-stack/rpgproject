"""
Description:
    Vue de combat standard contre des ennemis avec sélection de cible.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import arcade
import os
import arcade.gui
import Animations
from EnnemiesInGame import *
from PlayerInGame import *
from PlayerStats import*

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class FightScene(arcade.View):
    def __init__(self, compteur_maps,plr,Cleared_Levels):
        """
        Description:
            Initialise la scène de combat standard.
        Entrées:
            compteur_maps: progression des cartes.
            plr: instance du joueur.
            Cleared_Levels: niveaux déjà nettoyés.
        Sorties:
            Aucune.
        """
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

        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "perso.png"), scale=1)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 50

        self.Target = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "Target.png"), scale=.7)
        self.Target.center_x = 500
        self.Target.center_y = 500

        self.listeSprite = arcade.SpriteList()
        self.listeSprite.append(self.player_sprite)
        self.listeSprite.append(self.Target)

        self.plr = [plr, self.player_sprite, True]

        self.ViePlayer = arcade.SpriteList()
        self.BarreViePlayer=arcade.SpriteSolidColor(100, 20)
        self.BarreViePlayer.center_x = 100
        self.BarreViePlayer.center_y = 20
        self.bordureViePlayer=arcade.SpriteSolidColor(104, 24)
        self.bordureViePlayer.center_x = 100
        self.bordureViePlayer.center_y = 20
        self.bordureViePlayer.texture = arcade.make_soft_square_texture(24, arcade.csscolor.BLACK, outer_alpha=255)
        self.bordureViePlayer.width = 104

        self.ViePlayer.append(self.bordureViePlayer)
        self.ViePlayer.append(self.BarreViePlayer)

        self.tour=0

        self.ennemies = {}
        if self.compteur_maps < 6:
            self.nbEnemies = 1
        elif self.compteur_maps < 11:
            self.nbEnemies = 2
        else:
            self.nbEnemies = 3

        self.AllEnemy = SetUpEnemy(difficulte=self.compteur_maps, nbEnnemi=self.nbEnemies)

        self.healthBars = arcade.SpriteList()
        self.Healths = []
        self.bordureVie=[]

        self.fight_music = arcade.Sound(os.path.join(os.path.dirname(__file__), "..", "Sounds", "musicfight.mp3"), False)
        self.sonjoue = self.fight_music.play(volume=0.2)

        self.batch = arcade.shape_list.ShapeElementList()

        for i in range(self.nbEnemies):
            if self.AllEnemy.GetAllEnnemies()[i][0] == "Singe":
                self.ennemies[i] = [self.AllEnemy.ennemies[i],
                                    arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "banana.png"), scale=0.5),
                                    False]
            elif self.AllEnemy.GetAllEnnemies()[i][0] == "Araignee":
                self.ennemies[i] = [self.AllEnemy.ennemies[i],
                                    arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "spider.png"), scale=0.06),
                                    False]
            elif self.AllEnemy.GetAllEnnemies()[i][0] == "Gorille":
                self.ennemies[i] = [self.AllEnemy.ennemies[i],
                                    arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "gorilla.png"), scale=0.4),
                                    False]
            elif self.AllEnemy.GetAllEnnemies()[i][0] == "Oazo":
                self.ennemies[i] = [self.AllEnemy.ennemies[i],
                                    arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "ouaso.png"), scale=0.4),
                                    False]
            elif self.AllEnemy.GetAllEnnemies()[i][0] == "Gro-oazo":
                self.ennemies[i] = [self.AllEnemy.ennemies[i],
                                    arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "groazo.png"), scale=0.6),
                                    False]
            elif self.AllEnemy.GetAllEnnemies()[i][0] == "Ours":
                self.ennemies[i] = [self.AllEnemy.ennemies[i],
                                    arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "ours.png"), scale=0.4),
                                    False]


            self.ennemies[i][1].center_x = 500 - 200 * i
            self.ennemies[i][1].center_y = 500
            self.listeSprite.append(self.ennemies[i][1])

            healthBar = arcade.SpriteSolidColor(int((self.ennemies[i][0][2]*100)/self.ennemies[i][0][1]), 20)
            healthBar.center_x = 500 - 200 * i
            healthBar.center_y = 400
            self.healthBars.append(healthBar)
            self.Healths.append(self.ennemies[i][0][2])
            self.bordureVie.append(arcade.shape_list.create_rectangle_filled(500-200*i,400,104,24, arcade.csscolor.BLACK))
            self.batch.append(self.bordureVie[i])

        self.V = arcade.create_text_sprite("Victoire", arcade.csscolor.RED, 50)
        self.V.center_x = 300
        self.V.center_y = 300
        self.text_list = arcade.SpriteList()
        self.text_list.append(self.V)

        # Cartable
        self.SacGraphique=arcade.SpriteList()
        self.SacItems=arcade.SpriteList()
        self.clicked=False

        # Forme du sac
        self.SacStorage=self.plr[0].GetPlayerWeapons()
        for h in range(len(self.SacStorage)):
            for l in range(len(self.SacStorage[0])):
                case=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "fond_sac.png"), scale=0.227)
                case.center_x=300+100*l
                case.center_y=100+100*h
                case.pos=f"{h}{l}"
                self.SacGraphique.append(case)
                if self.SacStorage[h][l]==1:
                    BrancheImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "branche.png"), scale=0.5)
                    BrancheImage.center_x=297+100*l
                    BrancheImage.center_y=105+100*h
                    self.SacItems.append(BrancheImage)
                elif self.SacStorage[h][l]==2:
                    BananeImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "banane.png"), scale=0.25)
                    BananeImage.center_x=300+100*l
                    BananeImage.center_y=100+100*h
                    self.SacItems.append(BananeImage)
                elif self.SacStorage[0][l]==3:
                    H2FImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "H2F.png"), scale=0.25)
                    H2FImage.center_x=300+100*l
                    H2FImage.center_y=150
                    self.SacItems.append(H2FImage)
                elif self.SacStorage[h][l]==4:
                    EpeerouilleeImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "epee rouillee.png"), scale=0.2190)
                    EpeerouilleeImage.center_x=300+100*l
                    EpeerouilleeImage.center_y=100+100*h
                    self.SacItems.append(EpeerouilleeImage)    
                elif self.SacStorage[h][l]==5:
                    LanceImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "lance.png"), scale=0.25)
                    LanceImage.center_x=300+100*l
                    LanceImage.center_y=100+100*h
                    self.SacItems.append(LanceImage)    


    def on_show_view(self):
        """
        Description:
            Active la vue de combat.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

    def on_hide_view(self):
        """
        Description:
            Stoppe la musique lors de la sortie.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.fight_music.stop(self.sonjoue)

    def on_update(self, delta_time):
        """
        Description:
            Met à jour les états du combat et les transitions.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        self.listeSprite.update()

        for i in range(self.nbEnemies):
            self.Healths[i] = self.ennemies[i][0][2]

        if not self.victory and all(h == 0 for h in self.Healths):
            self.victory = True
            self.victory_timer = 0
            self.Target.alpha = 0

        if self.victory:
            self.victory_timer += delta_time
            if self.victory_timer >= 1:
                from Map import Map
                self.window.show_view(Map(self.plr[0],self.compteur_maps,self.Cleared_Levels))

        if self.plr[0].vie == 0:
            self.victory_timer += delta_time
            if self.victory_timer >= 1:
                from Spawn import Spawn
                self.window.show_view(Spawn())

        if self.Healths[self.enemySelected] == 0:
            for i in range(self.nbEnemies):
                if self.Healths[i] != 0 and self.Healths[self.enemySelected] == 0:
                    self.enemySelected = i
                    self.Target.center_x = 500 - 200 * i
                    self.Target.scale=.7,.7

        self.Target.angle += 0.2
        if self.Target.scale[0]>.01:
            self.Target.add_scale(-.005)

    def on_draw(self):
        """
        Description:
            Dessine la scène de combat et l'inventaire.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
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
        self.ViePlayer.draw()
        self.healthBars.draw()

        if self.victory:
            self.text_list.draw()
        elif self.tour == 0:
            self.SacGraphique.draw()
            self.SacItems.draw()

    def on_mouse_press(self, x, y, button, modifier):
        """
        Description:
            Gère la sélection de cible et l'utilisation d'objets.
        Entrées:
            x: position x de la souris.
            y: position y de la souris.
            button: bouton pressé.
            modifier: modificateurs.
        Sorties:
            Aucune.
        """
        if button == 1 and not self.clicked and not self.victory:
            if x > 410 and x < 600 and y > 410 and y < 600 and self.enemySelected != 0:
                self.enemySelected = 0
                self.Target.center_x = 500
                self.Target.scale=.7,.7
            elif x > 210 and x < 400 and y > 410 and y < 600 and self.nbEnemies >= 2 and self.enemySelected != 1:
                self.enemySelected = 1
                self.Target.center_x = 500 - 200 * 1
                self.Target.scale=.7,.7
            elif x > 0 and x < 200 and y > 410 and y < 600 and self.nbEnemies >= 3 and self.enemySelected != 2:
                self.enemySelected = 2
                self.Target.center_x = 500 - 200 * 2
                self.Target.scale=.7,.7
            
            ItemClicked=arcade.get_sprites_at_point((x,y),self.SacGraphique)
            if ItemClicked!=[]:
                if self.SacStorage[int(ItemClicked[0].pos[0])][int(ItemClicked[0].pos[1])] !=0:
                    self.clicked=True
                    Animations.Attaquer(self.plr, self.AllEnemy, self.SacStorage[int(ItemClicked[0].pos[0])][int(ItemClicked[0].pos[1])], self.enemySelected)
                    # self.plr,self.AllEnemy,1,0 --> Attaque l'ennemie 0 avec la branche
                    # self.ennemies[0],self.plr,1 --> Attaque le joueur avec l'ennemie 0 avec la branche
                    self.tour=1
                    arcade.schedule(self.SetUpTours, 1/60)

    def SetUpTours(self,delta_time):
        """
        Description:
            Prépare l'alternance des tours.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        self.decalage = 0
        arcade.unschedule(self.SetUpTours)
        arcade.schedule(self.enemyTour, .2)

    def enemyTour(self,delta_time):
        """
        Description:
            Exécute le tour des ennemis.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        self.EnnemieEnVie = 0
        for vie in self.Healths:
            if vie != 0:
                self.EnnemieEnVie+=1
        if self.tour>self.EnnemieEnVie:
            arcade.unschedule(self.enemyTour)
            self.tour = 0
            self.clicked=False
        else:
            for i in range(self.nbEnemies):
                if self.Healths[self.tour-1+self.decalage]==0:
                    self.decalage+=1
            if self.Healths[self.tour-1+self.decalage]!=0:
                Animations.Attaquer(self.ennemies[self.tour-1+self.decalage],self.plr,1)
            self.tour+=1

if __name__ == "__main__":
    window = arcade.Window(600, 600, "FightScene")
    FightScene_view = FightScene(1,player(),1)
    window.show_view(FightScene_view)
    arcade.run()