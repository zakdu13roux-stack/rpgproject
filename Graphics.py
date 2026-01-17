import arcade
import os

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Main Fenêtre", False, False)
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

        # Sprite du joueur
        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "perso.png"), scale=0.5)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Limite de la map
        self.map_width = 1200
        self.map_height = 100000  # Grande valeur pour simuler l'infini

        # Vitesse du joueur
        self.player_speed = 5

        # Camera
        self.camera = arcade.Camera2D()

    def on_draw(self):
        self.clear()

        # Définir la vue pour suivre le joueur

        self.camera.use()

        # Carrés d'herbe
        arcade.draw_rect_filled(arcade.rect.XYWH(0, 0, 400, 9999), arcade.csscolor.GREEN)
        arcade.draw_rect_filled(arcade.rect.XYWH(800, 0, 800, 9999), arcade.csscolor.GREEN)

        # Arbres
        image_path = os.path.join(os.path.dirname(__file__), "Images", "Arbre.png")
        texture = arcade.load_texture(image_path)
        scale = 0.3

        # Calculer la plage d'indices pour les arbres autour de la caméra
        min_i = int((self.camera.position[1] - self.height * 2) / 300)
        max_i = int((self.camera.position[1] + self.height * 2) / 300) + 1
        for i in range(min_i, max_i):
            y = i * 300
            # Offset basé sur i pour variété fixe
            offset_left = abs(hash(i)) % 3 * 20
            x_left = 80 + offset_left
            arcade.draw_texture_rect(texture, arcade.XYWH(x_left, y, texture.width, texture.height).scale(scale))

            offset_right = abs(hash(i + 1000)) % 3 * 20
            x_right = 530 + offset_right
            arcade.draw_texture_rect(texture, arcade.XYWH(x_right, y, texture.width, texture.height).scale(scale))


        # Trottoirs
        arcade.draw_line(201, -100000, 201, 100000, arcade.csscolor.BLACK)
        arcade.draw_line(399.5, -100000, 399.5, 100000, arcade.csscolor.BLACK)

        # Dessiner les sprites
        self.player_list.draw()

    def center_camera_on_player(self):
        screen_width = self.width
        screen_height = self.height

        camera_x = screen_width / 2
        camera_y = self.player_sprite.center_y

        self.camera.position = (camera_x, camera_y)



    def on_update(self, delta_time):
        # Mettre à jour les sprites
        self.player_list.update()
        self.player_sprite.center_x = max(0, min(self.player_sprite.center_x, self.width))
        # Pas de clamp sur y pour scrolling infini
        self.center_camera_on_player()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:  # Gauche
            self.player_sprite.change_x = -self.player_speed
        elif key == arcade.key.D:  # Droite
            self.player_sprite.change_x = self.player_speed
        elif key == arcade.key.Z:  # Haut
            self.player_sprite.change_y = self.player_speed
        elif key == arcade.key.S:  # Bas
            self.player_sprite.change_y = -self.player_speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.Q or key == arcade.key.D:
            self.player_sprite.change_x = 0
        if key == arcade.key.Z or key == arcade.key.S:
            self.player_sprite.change_y = 0

game = MyGame()
arcade.run()


