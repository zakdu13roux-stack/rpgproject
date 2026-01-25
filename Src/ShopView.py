import arcade
import arcade.gui
from Spawn import Spawn
from PlayerStats import *

class ShopView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        #Sprites
        potion_vie = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "potionverte.png"), scale = 0.3)
        potion_vie.center_x=150
        potion_vie.center_y= 375

        self.list_items = arcade.SpriteList()
        self.list_items.append(potion_vie)


        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=2, vertical_spacing=0, horizontal_spacing=0)

        #Items Shop
        self.stat_vie = GetLife()

        # Prix Shop
        self.prix_vie = self.stat_vie + 50

        # Boutons du menu
        return_button = arcade.gui.UIFlatButton(text="Return", width=200, height=50)
        self.buy_button = arcade.gui.UIFlatButton(text=str(self.prix_vie), width=100, height=50)

        # Ajouter les boutons à la grille
        self.grid.add(return_button, col_num=1, row_num=0)


        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="left", anchor_y="bottom")

        anchor_buy = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy.add(child = self.buy_button, align_x=-150, align_y=0)


        @self.buy_button.event("on_click")
        def on_click_buy_buttun(event):
            self.buy_button.text = str(self.prix_vie)
            print(self.buy_button.text)
            if self.prix_vie<=GetArgent():
                AddLife(50)
                AddArgent(-int(self.prix_vie))
                self.prix_vie = GetLife() +50


        @return_button.event("on_click")
        def on_click_return_button(event):
            spawn_view = Spawn(1)
            self.window.show_view(spawn_view)

    def on_update(self,delta_time):
        pass


    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.draw()
        self.list_items.draw()
        arcade.draw_text("Portefeuille : " + str(GetArgent()),70,570, arcade.csscolor.BLACK,17)

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