import arcade
import arcade.gui
import os



class Spawn(arcade.View):
    def __init__(self, compteur_maps):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.GREEN)
        print(compteur_maps)

        #compteur cleared_maps
        self.compteur_maps = compteur_maps

        # Sprite du joueur
        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "perso.png"), scale=0.3)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        #Sprite du shop
        self.shop_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "SHOP.png"), scale=0.3)
        self.shop_sprite.center_x = 100
        self.shop_sprite.center_y = 450
        self.deco_list= arcade.SpriteList()
        self.deco_list.append(self.shop_sprite)

        #Sprite Portail
        self.portal_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__),"Images","portal.png"),scale = 0.3)
        self.portal_sprite.center_x = 550
        self.portal_sprite.center_y = 300
        self.portal_list = arcade.SpriteList()
        self.portal_list.append(self.portal_sprite)

        # Limite de la map
        self.map_width = 1200
        self.map_height = 1200

        # Vitesse du joueur
        self.player_speed = 5

        self.batch = arcade.shape_list.ShapeElementList()

        path1 = arcade.shape_list.create_rectangle_filled(0,self.map_height/4,self.map_width,self.map_height/7,arcade.csscolor.BLANCHED_ALMOND)
        path2 = arcade.shape_list.create_rectangle_filled(self.map_width/4,0,self.map_width/7,self.map_height,arcade.csscolor.BLANCHED_ALMOND)

        self.batch.append(path1)
        self.batch.append(path2)


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
            from Menu import MenuView
            menu_view = MenuView(self.compteur_maps)
            self.window.show_view(menu_view)

        # Anchor pour positionner le bouton
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        self.anchor.add(anchor_x="right",anchor_y="top", child= self.spawn_button)

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.GREEN)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()


    def on_draw(self):
        self.clear()

        self.batch.draw()


        # Définir la vue pour suivre le joueur
        self.camera.use()

        # Entrer dans le magazin
        if self.hit:
            from ShopView import ShopView
            shop_view = ShopView(self.compteur_maps)
            self.window.show_view(shop_view)

        # Dessiner les sprites
        self.portal_list.draw()
        self.player_list.draw()
        self.deco_list.draw()
        self.manager.draw()


    def center_camera_on_player(self):
        screen_width = self.width
        screen_height = self.height

        camera_x = screen_width / 2
        camera_y = screen_height / 2

        self.camera.position = (camera_x, camera_y)



    def on_update(self, delta_time):
        # Mettre à jour les sprites
        self.player_list.update()
        self.player_sprite.center_x = max(0, min(self.player_sprite.center_x, self.width))
        self.player_sprite.center_y = max(0, min(self.player_sprite.center_y, self.height))


        self.center_camera_on_player()

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
            map_view = Map(self.compteur_maps)
            self.window.show_view(map_view)


    def on_key_press(self, key, modifiers):
        pas = arcade.load_sound("Sounds/pas.wav")
        if key == arcade.key.Q :# Gauche
            pas.play()
            self.player_sprite.change_x = -self.player_speed
        elif key == arcade.key.D:  # Droite
            pas.play()
            self.player_sprite.change_x = self.player_speed
        elif key == arcade.key.Z:  # Haut
            pas.play()
            self.player_sprite.change_y = self.player_speed
        elif key == arcade.key.S:  # Bas
            pas.play()
            self.player_sprite.change_y = -self.player_speed


    def on_key_release(self, key, modifiers):
        if key == arcade.key.Q or key == arcade.key.D:
            self.player_sprite.change_x = 0
        if key == arcade.key.Z or key == arcade.key.S:
            self.player_sprite.change_y = 0

# Main application setup
if __name__ == "__main__":
    window = arcade.Window(600, 600, "RPG Game with Menu")
    spawn_view = Spawn(1)
    window.show_view(spawn_view)
    arcade.run()