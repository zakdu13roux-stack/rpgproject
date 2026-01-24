import arcade
import arcade.gui
from Spawn import Spawn
from PlayerStats import *
from PlayerInGame import *

class StatueView(arcade.View):
    def __init__(self,compteur_maps, player):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.compteur_maps = compteur_maps
        self.player = player
        
        #Sprites
        potion_vie = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "potionverte.png"), scale = 0.3)
        potion_vie.center_x=150
        potion_vie.center_y= 375    

        Argent = arcade.Sprite(os.path.join(os.path.dirname(__file__), "Images", "coins.png"), scale = 0.3)
        Argent.center_x= 400
        Argent.center_y= 375

        self.list_items = arcade.SpriteList()
        self.list_items.append(Argent)
        self.list_items.append(potion_vie)

        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=2, vertical_spacing=0, horizontal_spacing=0)

        #Items Shop
        self.stat_vie = GetLife()

        # Prix Shop
        self.prix_vie = self.stat_vie + 50

        # Boutons du menu
        return_button = arcade.gui.UIFlatButton(text="Return", width=200, height=50)
        self.life_button = arcade.gui.UIFlatButton(text="Life", width=100, height=50)
        self.coins_button = arcade.gui.UIFlatButton(text="Coins", width=100, height=50)

        # Ajouter les boutons à la grille
        self.grid.add(return_button, col_num=1, row_num=0)


        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="left", anchor_y="bottom")

        anchor_buy = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy.add(child = self.life_button, align_x=-150, align_y=0)

        anchor_buy = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy.add(child = self.coins_button, align_x=0, align_y=0)


        @self.life_button.event("on_click")
        def on_click_life_button(event):
            self.life_button.text = "Life"
            self.player.heal(50)
            from Map import Map
            Map_view = Map(self.compteur_maps, self.player)
            self.window.show_view(Map_view)

        @self.coins_button.event("on_click")
        def on_click_coins_button(event):
            AddArgent(100)
            from Map import Map
            Map_view = Map(self.compteur_maps, self.player)
            self.window.show_view(Map_view)

        @return_button.event("on_click")
        def on_click_return_button(event):
            from Map import Map
            Map_view = Map(self.compteur_maps, self.player)
            self.window.show_view(Map_view)

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
    menu_view = StatueView(1,player())
    window.show_view(menu_view)
    arcade.run()