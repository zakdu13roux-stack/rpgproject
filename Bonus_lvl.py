import arcade
import os
import arcade.gui
import Map
import StatueView


class Bonus_lvl(arcade.View):
    def __init__(self,cpt):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        self.compteur = cpt

        self.grille = arcade.gui.UIGridLayout(columns=1,vertical_spacing=0,horizontal_spacing=0)

        return_button = arcade.gui.UIFlatButton(text="Return",width=100,height=50)
        return_button.center_x=0
        return_button.center_y=0

        self.grille.add(return_button,0,0)

        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grille, anchor_x="left", anchor_y="bottom")


        self.text_list = arcade.SpriteList()

        # Sprite du joueur
        self.player_sprite = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "perso.png"), scale=0.3)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Vitesse du joueur
        self.player_speed = 5

        self.hit = False

        # Sprites décor
        self.decor_list = arcade.SpriteList()

        self.statue = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "statue.png"), scale=0.8)

        self.statue.center_x = 300
        self.statue.center_y = 365

        self.statue_list = arcade.SpriteList() 
        self.statue_list.append(self.statue)

        self.sol = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "bonus_floor.jpg"), scale=0.5)
        self.sol2 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "bonus_floor.jpg"), scale=0.5)
        self.sol3 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "bonus_floor.jpg"), scale=0.5)
        self.sol4 = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "bonus_floor.jpg"), scale=0.5)

        self.sol.center_x = -60
        self.sol.center_y = 450

        self.sol2.center_x = 400
        self.sol2.center_y = 450

        self.sol3.center_x = 660
        self.sol3.center_y = 150

        self.sol4.center_x = 200
        self.sol4.center_y = 150



        self.decor_list.append(self.sol)
        self.decor_list.append(self.sol2)
        self.decor_list.append(self.sol3)
        self.decor_list.append(self.sol4) 

        

        @return_button.event("on_click")
        def on_click_return_button(event):
            map_view = Map.Map(self.compteur)
            self.window.show_view(map_view)

    def on_draw(self):
        self.clear()
        self.decor_list.draw()
        self.statue_list.draw()
        self.player_list.draw()
        self.text_list.draw()
        self.manager.draw()

        # Utiliser la statue pour interagir
        if self.hit:
            from StatueView import StatueView
            statue_view = StatueView(self.compteur)
            self.window.show_view(statue_view)


    def on_update(self, delta_time):
        # Mettre à jour les sprites
        self.player_list.update()
        self.player_sprite.center_x = max(0, min(self.player_sprite.center_x, self.width))
        self.player_sprite.center_y = max(0, min(self.player_sprite.center_y, self.height))

        if arcade.check_for_collision_with_list(self.player_sprite, self.statue_list):
            self.hit = True
        else:
            self.hit = False

        if arcade.check_for_collision_with_list(self.player_sprite,self.statue_list):
            self.teleport = True
        else:
            self.teleport = False
        if self.teleport == True:
            from StatueView import StatueView
            statue_view = StatueView(self.compteur)
            self.window.show_view(statue_view)


    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

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


if __name__ == "__main__":
    window = arcade.Window(600,600,"Bonus Level")
    game = Bonus_lvl(1)
    window.show_view(game)
    arcade.run()
