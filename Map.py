import arcade
import os
from random import randint
from FightScene import FightScene

class Map(arcade.View):
    def __init__(self,cpt):
        super().__init__()

        # Compteur cleared maps
        self.compteur = cpt
        self.text_compteur = arcade.create_text_sprite( "Cleared maps : " + str(self.compteur),arcade.csscolor.BLACK,17)
        self.text_compteur.center_x = 75
        self.text_compteur.center_y = 570
        self.texts = arcade.SpriteList()
        self.texts.append(self.text_compteur)

        # Sprite du joueur
        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "perso.png"), scale=0.3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 500
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Sprite icones map
        self.icon_start = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "start.png"), scale=0.3)
        self.icon_sprite1 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "area.png"), scale=0.3)
        self.icon_sprite2 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "area.png"), scale=0.3)
        self.icon_sprite3 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "area.png"), scale=0.3)
        self.icon_end = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "end.png"), scale=0.3)

        self.icon_start.center_x = 95
        self.icon_start.center_y = 500

        self.icon_sprite1.center_x = 300
        self.icon_sprite1.center_y = 450

        self.icon_sprite2.center_x = 300
        self.icon_sprite2.center_y = 250

        self.icon_sprite3.center_x = 300
        self.icon_sprite3.center_y = 50

        self.icon_end.center_x = 495
        self.icon_end.center_y = 100


        self.icon_list = arcade.SpriteList()
        self.icon_list.append(self.icon_start)
        self.icon_list.append(self.icon_sprite1)
        self.icon_list.append(self.icon_sprite2)
        self.icon_list.append(self.icon_sprite3)
        self.icon_list.append(self.icon_end)

        # Sprites décor
        self.pelouse1 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse1.center_x = 115
        self.pelouse1.center_y = 115

        self.pelouse2 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse2.center_x = 350
        self.pelouse2.center_y = 350

        self.pelouse3 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse3.center_x = 115
        self.pelouse3.center_y = 350

        self.pelouse4 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse4.center_x = 350
        self.pelouse4.center_y = 115

        self.pelouse5 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse5.center_x = 575
        self.pelouse5.center_y = 115

        self.pelouse6 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse6.center_x = 575
        self.pelouse6.center_y = 350

        self.pelouse7 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse7.center_x = 350
        self.pelouse7.center_y = 575

        self.pelouse8 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse8.center_x = 115
        self.pelouse8.center_y = 575

        self.pelouse9 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "herbe.webp"), scale =0.5)
        self.pelouse9.center_x = 570
        self.pelouse9.center_y = 575

        self.trucs_tt_devant_list = arcade.SpriteList()
        self.trucs_tt_devant_list.append(self.pelouse1)
        self.trucs_tt_devant_list.append(self.pelouse2)
        self.trucs_tt_devant_list.append(self.pelouse3)
        self.trucs_tt_devant_list.append(self.pelouse4)
        self.trucs_tt_devant_list.append(self.pelouse5)
        self.trucs_tt_devant_list.append(self.pelouse6)
        self.trucs_tt_devant_list.append(self.pelouse7)
        self.trucs_tt_devant_list.append(self.pelouse8)
        self.trucs_tt_devant_list.append(self.pelouse9)

        self.arbre1 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Arbre.png"), scale = 0.3)
        self.arbre2 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Arbre.png"), scale = 0.3)
        self.arbre3 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Arbre.png"), scale = 0.3)
        self.arbre4 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Arbre.png"), scale = 0.3)
        self.arbre5 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Arbre.png"), scale = 0.3)

        self.arbre1.center_x = randint(40,250)
        self.arbre1.center_y = randint(40,350)

        self.arbre2.center_x = randint(40,250)
        self.arbre2.center_y = randint(40,350)

        self.arbre3.center_x = randint(350,560)
        self.arbre3.center_y = randint(250,560)

        self.arbre4.center_x = randint(350,560)
        self.arbre4.center_y = randint(250,560)

        self.arbre5.center_x = randint(50,550)
        self.arbre5.center_y = randint(50,550)

        self.rock1 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Rock.png"), scale = 0.2)
        self.rock2 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Rock.png"), scale = 0.2)
        self.rock3 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Rock.png"), scale = 0.2)
        self.rock4 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "Rock.png"), scale = 0.2)

        self.rock1.center_x = randint(40,250)
        self.rock1.center_y = randint(40,350)

        self.rock2.center_x = randint(40,250)
        self.rock2.center_y = randint(40,350)

        self.rock3.center_x = randint(350,560)
        self.rock3.center_y = randint(250,560)

        self.rock4.center_x = randint(350,560)
        self.rock4.center_y = randint(250,560)


        self.decor_list = arcade.SpriteList()
        self.decor_list.append(self.rock1)
        self.decor_list.append(self.rock2)
        self.decor_list.append(self.rock3)
        self.decor_list.append(self.rock4)
        self.decor_list.append(self.arbre1)
        self.decor_list.append(self.arbre2)
        self.decor_list.append(self.arbre3)
        self.decor_list.append(self.arbre4)
        self.decor_list.append(self.arbre5)

        # Limite de la map
        self.map_width = 1200
        self.map_height = 1200

        # Vitesse du joueur
        self.player_speed = 5

        self.batch = arcade.shape_list.ShapeElementList()

        path1 = arcade.shape_list.create_line(100,500,300,500,arcade.csscolor.BLACK,25)
        path2 = arcade.shape_list.create_line(300,500,300,300,arcade.csscolor.BLACK,25)
        path3 = arcade.shape_list.create_line(300,300,300,100,arcade.csscolor.BLACK,25)
        path4 = arcade.shape_list.create_line(300,100,500,100,arcade.csscolor.BLACK,25)

        self.batch.append(path1)
        self.batch.append(path2)
        self.batch.append(path3)
        self.batch.append(path4)

        # Camera
        self.camera = arcade.Camera2D()

    def on_draw(self):
        self.clear()

        # Dessiner les sprites
        self.trucs_tt_devant_list.draw()
        self.batch.draw()
        self.icon_list.draw()
        self.player_list.draw()
        self.decor_list.draw()
        self.texts.draw()

        # Définir la vue pour suivre le joueur
        self.camera.use()


    def center_camera_on_player(self):
        screen_width = self.width
        screen_height = self.height

        camera_x = screen_width / 2
        camera_y = screen_height / 2

        self.camera.position = (camera_x, camera_y)

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.GREEN)



    def on_update(self, delta_time):
        # Mettre à jour les sprites
        self.player_list.update()
        self.player_sprite.center_x = max(0, min(self.player_sprite.center_x, self.width))
        self.player_sprite.center_y = max(0, min(self.player_sprite.center_y, self.height))
        # Pas de clamp sur y pour scrolling infini
        self.center_camera_on_player()


    def on_key_press(self, key, modifiers):
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
            elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 500:
                fight_scene_view = FightScene()
                self.window.show_view(fight_scene_view)
            elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 300:
                fight_scene_view = FightScene()
                self.window.show_view(fight_scene_view)
            elif self.player_sprite.center_x == 300 and self.player_sprite.center_y == 100:
                fight_scene_view = FightScene()
                self.window.show_view(fight_scene_view)
            elif self.player_sprite.center_x == 500 and self.player_sprite.center_y > 100:
                self.window.show_view(Map(self.compteur+1))
                self.text_compteur = self.compteur






if __name__ == "__main__":
    window = arcade.Window(600,600,"Fights")
    game = Map(0)
    window.show_view(game)
    arcade.run()

