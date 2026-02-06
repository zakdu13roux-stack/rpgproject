import arcade
import arcade.gui
from Spawn import Spawn
from PlayerStats import *

class main(arcade.View):
    def __init__(self):
        """
        Description:
            Initialise la boutique.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        super().__init__()
        self.manager = arcade.gui.UIManager()

        # Background
        sky_background = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "TITLE.png"), scale = 1)
        sky_background.center_x= 300
        sky_background.center_y= 300

        self.list_decor = arcade.SpriteList()
        self.list_decor.append(sky_background)

        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=2, vertical_spacing=0, horizontal_spacing=0)

        # Boutons du menu
        return_button = arcade.gui.UIFlatButton(text="Play", width=150, height=80)

        # Ajouter les boutons à la grille
        self.grid.add(return_button, col_num=1, row_num=0)

        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        anchor.add(child=self.grid, anchor_x="center_x", anchor_y="bottom")

        @return_button.event("on_click")
        def on_click_return_button(event):
            """
            Description:
                Retourne au spawn.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            spawn_view = Spawn()
            self.window.show_view(spawn_view)

    def on_update(self,delta_time):
        """
        Description:
            Met à jour la boutique.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        pass


    def on_draw(self):
        """
        Description:
            Dessine la boutique et le portefeuille.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.clear()
        self.list_decor.draw()
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.draw()

    def on_show_view(self):
        """
        Description:
            Active la vue de boutique.
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
            Désactive l'UI manager.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.manager.disable()


if __name__ == "__main__":
    window = arcade.Window(600,600,"Main Menu")
    game = main()
    window.show_view(game)
    arcade.run()
