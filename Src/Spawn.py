"""
Description:
    Vue de départ avec déplacement, shop et portail vers la carte.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import arcade
import arcade.gui
import os
from PlayerStats import*
from PlayerInGame import*



class Spawn(arcade.View):
    def __init__(self):
        """
        Description:
            Initialise la zone de départ.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        super().__init__()
        arcade.set_background_color(arcade.csscolor.GREEN)

        # Charger les sons
        self.pas = arcade.load_sound(os.path.join(os.path.dirname(__file__), "..", "Sounds", "pas.wav"))

        # Sprite du joueur
        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "perso.png"), scale=0.3)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        #Sprite du shop
        self.shop_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "SHOP.png"), scale=0.3)
        self.shop_sprite.center_x = 100
        self.shop_sprite.center_y = 450
        self.deco_list= arcade.SpriteList()
        self.deco_list.append(self.shop_sprite)

        #Sprite Portail
        self.portal_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__),"..","Images","portal.png"),scale = 0.3)
        self.portal_sprite.center_x = 550
        self.portal_sprite.center_y = 320
        self.portal_list = arcade.SpriteList()
        self.portal_list.append(self.portal_sprite)

        # Limite de la map
        self.map_width = 1200
        self.map_height = 1200

        # Vitesse du joueur
        self.player_speed = 5

        herbe_topleft = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "herbe.webp"), scale=1)
        herbe_topleft.center_x = 0
        herbe_topleft.center_y = 400
        herbe_topright = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "herbe.webp"), scale=1)
        herbe_topright.center_x = 400
        herbe_topright.center_y = 400
        herbe_bottomleft = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "herbe.webp"), scale=1)
        herbe_bottomleft.center_x = 0
        herbe_bottomleft.center_y = 0
        herbe_bottomright = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "herbe.webp"), scale=1)
        herbe_bottomright.center_x = 400
        herbe_bottomright.center_y = 0

        self.herbizare = arcade.SpriteList()
        self.herbizare.append(herbe_topleft)
        self.herbizare.append(herbe_topright)
        self.herbizare.append(herbe_bottomleft)
        self.herbizare.append(herbe_bottomright)


        path1 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "pathcomplet.png"), scale=1.3)
        path1.center_x = 300
        path1.center_y = 300




        self.pathlist = arcade.SpriteList()
        self.pathlist.append(path1)



        # Camera
        self.camera = arcade.Camera2D()

        # Hitboxes
        self.hitboxe_basecolor=(255, 255, 255)
        self.hitboxe_collcolor =(0, 0, 255)
        self.hit = False
        self.teleport = False

        # UI manager
        self.manager = arcade.gui.UIManager()

        # Bouton Menu
        self.spawn_button = arcade.gui.UIFlatButton(x=450, y=0, text="Menu", width=100)
        @self.spawn_button.event("on_click")
        def on_click_resume_button(event):
            """
            Description:
                Ouvre le menu principal.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            from Menu import MenuView
            menu_view = MenuView()
            self.window.show_view(menu_view)

        # Anchor pour positionner le bouton
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        self.anchor.add(anchor_x="right",anchor_y="top", child= self.spawn_button)

        # Musique de fond
        self.menu_music = arcade.Sound(os.path.join(os.path.dirname(__file__), "..", "Sounds", "musicmenu.mp3"), False)
        self.sonjoue = self.menu_music.play(volume=GetVolume())

    def on_show_view(self):
        """
        Description:
            Active la vue de spawn.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        arcade.set_background_color(arcade.csscolor.GREEN)
        self.manager.enable()

    def on_hide_view(self):
        """
        Description:
            Désactive l'UI manager et stoppe la musique.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.menu_music.stop(self.sonjoue)
        self.manager.disable()


    def on_draw(self):
        """
        Description:
            Dessine la zone de départ.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.clear()
        self.herbizare.draw()

        self.pathlist.draw()


        # Définir la vue pour suivre le joueur
        self.camera.use()

        # Entrer dans le magazin
        if self.hit:
            from ShopView import ShopView
            shop_view = ShopView()
            self.window.show_view(shop_view)

        # Dessiner les sprites
        self.portal_list.draw()
        self.player_list.draw()
        self.deco_list.draw()
        self.manager.draw()


    def center_camera_on_player(self):
        """
        Description:
            Centre la caméra sur le joueur.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        screen_width = self.width
        screen_height = self.height

        camera_x = screen_width / 2
        camera_y = screen_height / 2

        self.camera.position = (camera_x, camera_y)



    def on_update(self, delta_time):
        """
        Description:
            Met à jour le joueur et gère les collisions.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        # Mettre à jour les sprites
        self.player_list.update()
        self.player_sprite.center_x = max(0, min(self.player_sprite.center_x, self.width))
        self.player_sprite.center_y = max(0, min(self.player_sprite.center_y, self.height))


        if arcade.check_for_collision_with_list(self.player_sprite, self.deco_list):
            self.hit = True
        else:
            self.hit = False

        if arcade.check_for_collision_with_list(self.player_sprite,self.portal_list):
            self.teleport = True
        else:
            self.teleport = False
        if self.teleport == True:
            from Map import Map
            map_view = Map(player=player())
            self.window.show_view(map_view)

    def on_key_press(self, key, modifiers):
        """
        Description:
            Gère les déplacements au clavier.
        Entrées:
            key: touche pressée.
            modifiers: modificateurs.
        Sorties:
            Aucune.
        """
        if key == arcade.key.Q :# Gauche
            self.player_sprite.change_x = -self.player_speed
            self.pas.play(volume=0.1)
        elif key == arcade.key.D:  # Droite
            self.player_sprite.change_x = self.player_speed
            self.pas.play(volume=0.1)
        elif key == arcade.key.Z:  # Haut
            self.player_sprite.change_y = self.player_speed
            self.pas.play(volume=0.1)
        elif key == arcade.key.S:  # Bas
            self.player_sprite.change_y = -self.player_speed
            self.pas.play(volume=0.1)


    def on_key_release(self, key, modifiers):
        """
        Description:
            Arrête le déplacement au relâchement des touches.
        Entrées:
            key: touche relâchée.
            modifiers: modificateurs.
        Sorties:
            Aucune.
        """
        if key == arcade.key.Q or key == arcade.key.D:
            self.player_sprite.change_x = 0
        if key == arcade.key.Z or key == arcade.key.S:
            self.player_sprite.change_y = 0

# Main application setup
if __name__ == "__main__":
    window = arcade.Window(600, 600, "RPG Game with Menu")
    spawn_view = Spawn()
    window.show_view(spawn_view)
    arcade.run()