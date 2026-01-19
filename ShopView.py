import arcade
import arcade.gui
from Spawn import Spawn
from PlayerStats import *

class ShopView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()



        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=2, vertical_spacing=0, horizontal_spacing=0)

        #Items Shop
        self.stat_vie = GetLife()

        # Prix Shop
        self.prix_vie = self.stat_vie + 50

        # Boutons du menu
        return_buttun = arcade.gui.UIFlatButton(text="Return", width=200, height=50)
        buy_buttun = arcade.gui.UIFlatButton(text=str(self.prix_vie), width=200, height=50)

        # Ajouter les boutons à la grille
        self.grid.add(buy_buttun, col_num=0, row_num=0)
        self.grid.add(return_buttun, col_num=1, row_num=0)


        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="center", anchor_y="center")


        @buy_buttun.event("on_click")
        def on_click_buy_buttun(event):
            UpdateLife(50)


        @return_buttun.event("on_click")
        def on_click_return_button(event):
            spawn_view = Spawn()
            self.window.show_view(spawn_view)

    def on_update(self,delta_time):
        pass


    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.draw()

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.GREEN)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

# Main application setup
if __name__ == "__main__":
    window = arcade.Window(600, 600, "RPG Game with Menu")
    menu_view = ShopView()
    window.show_view(menu_view)
    arcade.run()