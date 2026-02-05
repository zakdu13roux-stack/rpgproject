"""
Description:
    Vue de carte avec parcours de niveaux et transitions de scènes.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import arcade
import os
from random import randint
import arcade.gui
from PlayerInGame import player

class Map(arcade.View):
    def __init__(self,player,cpt=1,cleared_lvls=0):
        """
        Description:
            Initialise la carte de progression.
        Entrées:
            player: instance du joueur.
            cpt: compteur de cartes.
            cleared_lvls: niveaux déjà nettoyés.
        Sorties:
            Aucune.
        """
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.player = player

        # Compteur cleared maps
        self.compteur = cpt
        self.text_compteur = arcade.create_text_sprite("Cleared maps : " + str(self.compteur-1),arcade.csscolor.BLACK,17)
        self.text_compteur.center_x = 75
        self.text_compteur.center_y = 570
        self.texts = arcade.SpriteList()
        self.texts.append(self.text_compteur)

        # Indication commandes
        self.text_tuto = arcade.create_text_sprite("Enter Level :    Enter",arcade.csscolor.BLACK,17)
        self.text_tuto.center_x= 450
        self.text_tuto.center_y = 570
        self.texts.append(self.text_tuto)

        # Compteur cleared levels
        self.cleared_lvls= cleared_lvls

        # Sprite du joueur
        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "perso.png"), scale=0.28)
        if cleared_lvls == 0:
            self.player_sprite.center_x = 100
            self.player_sprite.center_y = 500
        elif cleared_lvls == 1:
            self.player_sprite.center_x = 300
            self.player_sprite.center_y = 500
        elif cleared_lvls == 2:
            self.player_sprite.center_x = 300
            self.player_sprite.center_y = 300
        else:
            self.player_sprite.center_x = 300
            self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)


        self.rectangle = arcade.shape_list.ShapeElementList()

        barre1 = arcade.shape_list.create_rectangle_filled(548,570,5,28,arcade.csscolor.BLACK)
        barre2 = arcade.shape_list.create_rectangle_filled(514,585,68,5,arcade.csscolor.BLACK)
        barre3 = arcade.shape_list.create_rectangle_filled(480,570,5,28,arcade.csscolor.BLACK)
        barre4 = arcade.shape_list.create_rectangle_filled(514,555,68,5,arcade.csscolor.BLACK)



        self.rectangle.append(barre1)
        self.rectangle.append(barre2)
        self.rectangle.append(barre3)
        self.rectangle.append(barre4)


        # Sprite icones map
        self.icon_start = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "start.png"), scale=0.3)
        self.icon_sprite1 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "battle.png"), scale=0.3)
        self.icon_sprite2 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "area.png"), scale=0.3)
        self.icon_sprite3 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "battle.png"), scale=0.3)
        if self.compteur%10!=0:
            self.icon_end = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "end.png"), scale=0.3)
        else:
            self.icon_end = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "bossmort.png"), scale=0.3)


        self.icon_start.center_x = 95
        self.icon_start.center_y = 500

        self.icon_sprite1.center_x = 300
        self.icon_sprite1.center_y = 500

        self.icon_sprite2.center_x = 300
        self.icon_sprite2.center_y = 290

        self.icon_sprite3.center_x = 300
        self.icon_sprite3.center_y = 90

        self.icon_end.center_x = 495
        self.icon_end.center_y = 100


        self.icon_list = arcade.SpriteList()
        self.icon_list.append(self.icon_start)
        self.icon_list.append(self.icon_sprite1)
        self.icon_list.append(self.icon_sprite2)
        self.icon_list.append(self.icon_sprite3)
        self.icon_list.append(self.icon_end)

        # Chemins
        self.path = arcade.shape_list.ShapeElementList()

        path1 = arcade.shape_list.create_line(100,500,300,500,arcade.csscolor.BLACK,25)
        path2 = arcade.shape_list.create_line(300,500,300,300,arcade.csscolor.BLACK,25)
        path3 = arcade.shape_list.create_line(300,300,300,100,arcade.csscolor.BLACK,25)
        path4 = arcade.shape_list.create_line(300,100,500,100,arcade.csscolor.BLACK,25)

        self.path.append(path1)
        self.path.append(path2)
        self.path.append(path3)
        self.path.append(path4)

        self.colPath = arcade.SpriteList()
        p1 = arcade.SpriteSolidColor(120,50,arcade.csscolor.BLACK)
        p1.center_x = 200
        p1.center_y = 500
        p1.alpha = 0
        p2 = arcade.SpriteSolidColor(50,330,arcade.csscolor.BLACK)
        p2.center_x = 300
        p2.center_y = 300
        p2.alpha = 0
        self.colPath = arcade.SpriteList()
        p3 = arcade.SpriteSolidColor(120,50,arcade.csscolor.BLACK)
        p3.center_x = 400
        p3.center_y = 100
        p3.alpha = 0
        self.colPath.append(p1)
        self.colPath.append(p2)
        self.colPath.append(p3)



        # Sprites décor arrière plan
        self.pelouse = {}
        for h in range(3):
            for l in range(3):
                self.pelouse[h*10+l]=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "herbe.webp"), scale =0.5)
                self.pelouse[h*10+l].center_x = 115+235*l
                self.pelouse[h*10+l].center_y = 115+235*h

        self.Herbe = arcade.SpriteList()
        for p in self.pelouse:
            self.Herbe.append(self.pelouse[p])

        # Sprites décor
        self.decor_list = arcade.SpriteList()

        self.arbres={}
        self.rock = {}
        for i in range(5):
            # Partie Arbre
            self.arbres[i] = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "Arbre.png"), scale = 0.3)
            self.arbres[i].center_x = randint(50,550)
            self.arbres[i].center_y = randint(50,550)
            if self.arbres != {}:
                tries = 0
                while (arcade.check_for_collision_with_list(self.arbres[i],self.decor_list) != [] or arcade.check_for_collision_with_list(self.arbres[i],self.icon_list) != [] or arcade.check_for_collision_with_list(self.arbres[i],self.colPath) != []) and tries < 10:
                    self.arbres[i].center_x = randint(50,550)
                    self.arbres[i].center_y = randint(50,550)
                    tries+=1
                if tries < 5:
                    self.decor_list.append(self.arbres[i])
            # Partie Rocher
            self.rock[i] = self.rock1 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "Rock.png"), scale = 0.2)
            self.rock[i].center_x = randint(50,550)
            self.rock[i].center_y = randint(50,550)
            if self.rock != {}:
                tries = 0
                while (arcade.check_for_collision_with_list(self.rock[i],self.decor_list) != [] or arcade.check_for_collision_with_list(self.rock[i],self.icon_list) != [] or arcade.check_for_collision_with_list(self.rock[i],self.colPath) != []) and tries < 10:
                    self.rock[i].center_x = randint(50,550)
                    self.rock[i].center_y = randint(50,550)
                    tries+=1
                if tries < 5:
                    self.decor_list.append(self.rock[i])



        # Limite de la map
        self.map_width = 1200
        self.map_height = 1200

        # Vitesse du joueur
        self.player_speed = 5

        # Camera
        self.camera = arcade.Camera2D()

    def on_draw(self):
        """
        Description:
            Dessine la carte et ses éléments.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.clear()

        # Dessiner les sprites
        self.Herbe.draw()
        self.path.draw()
        self.icon_list.draw()
        self.player_list.draw()
        self.decor_list.draw()
        self.texts.draw()
        self.manager.draw()
        self.rectangle.draw()

        # Définir la vue pour suivre le joueur
        self.camera.use()


    def on_show_view(self):
        """
        Description:
            Active la vue de la carte.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.enable()

    def on_hide_view(self):
        """
        Description:
            Désactive l'UI manager.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.manager.disable()

    def on_update(self, delta_time):
        """
        Description:
            Met à jour la position du joueur.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        # Mettre à jour les sprites
        self.player_list.update()
        self.player_sprite.center_x = max(0, min(self.player_sprite.center_x, self.width))
        self.player_sprite.center_y = max(0, min(self.player_sprite.center_y, self.height))


    def on_key_press(self, key, modifiers):
        """
        Description:
            Gère les déplacements et l'entrée en niveau.
        Entrées:
            key: touche pressée.
            modifiers: modificateurs.
        Sorties:
            Aucune.
        """
        if self.player_sprite.center_x == 100 and self.player_sprite.center_y == 500:
            if key == arcade.key.D:  # Droite
                self.player_sprite.strafe(200)
        elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 500:
            if key == arcade.key.Q:  # Gauche
                self.player_sprite.strafe(-200)
            elif key == arcade.key.S:  # Bas
                self.player_sprite.center_y -= 200
        elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 300:
            if key == arcade.key.Z:  # Haut:
                self.player_sprite.center_y += 200
            elif key == arcade.key.S:  # Bas
                self.player_sprite.center_y -= 200
        elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 100:
            if key == arcade.key.D:  # Droite
                self.player_sprite.strafe(200)
            elif key == arcade.key.Z:  # Haut
                self.player_sprite.center_y += 200
        elif self.player_sprite.center_x == 500 and self.player_sprite.center_y > 100:
            if key == arcade.key.Q:  # Gauche
                self.player_sprite.strafe(-200)
        if key == arcade.key.ENTER: # Lancer un combat
            if self.player_sprite.center_x == 100 and self.player_sprite.center_y == 500:
                pass
            elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 500 and self.cleared_lvls==0:
                self.cleared_lvls = 1
                from FightScene import FightScene
                fight_scene_view = FightScene(self.compteur, self.player,self.cleared_lvls)
                self.window.show_view(fight_scene_view)
            elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 300 and self.cleared_lvls==1:
                from Bonus_lvl import Bonus_lvl
                self.cleared_lvls = 2
                bonus_lvl_view = Bonus_lvl(self.compteur,self.player, self.cleared_lvls)
                self.window.show_view(bonus_lvl_view)
            elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 100 and (self.cleared_lvls==1 or self.cleared_lvls==2):
                self.cleared_lvls = 3
                from FightScene import FightScene
                fight_scene_view = FightScene(self.compteur, self.player,self.cleared_lvls)
                self.window.show_view(fight_scene_view)
            elif self.player_sprite.center_x == 500 and self.player_sprite.center_y > 100 and self.cleared_lvls==3:
                if self.compteur%10 !=0 :
                    self.window.show_view(Map(self.player,self.compteur+1,0))
                    self.text_compteur = self.compteur
                else:
                    from BossFight import BossFight
                    BossFight_View = BossFight(self.player,self.compteur+1,0)
                    self.window.show_view(BossFight_View)
                    self.text_compteur = self.compteur





if __name__ == "__main__":
    window = arcade.Window(600,600,"Map")
    game = Map(player())
    window.show_view(game)
    arcade.run()

