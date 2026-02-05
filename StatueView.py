"""
Description:
    Vue de récompense de statue avec choix vie ou pièces.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import arcade
import arcade.gui
from Spawn import Spawn
from PlayerStats import *
from PlayerInGame import *

class StatueView(arcade.View):
    def __init__(self,compteur_maps, player, cleared_lvls):
        """
        Description:
            Initialise la vue de récompense de la statue.
        Entrées:
            compteur_maps: progression des cartes.
            player: instance du joueur.
            cleared_lvls: niveaux déjà nettoyés.
        Sorties:
            Aucune.
        """
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.compteur_maps = compteur_maps
        self.player = player
        self.cleared_lvls = cleared_lvls

        #Sprites
        potion_vie = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "potionverte.png"), scale = 0.167)
        potion_vie.center_x = 200
        potion_vie.center_y = 365

        Argent = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "coins.png"), scale = 0.3)
        Argent.center_x = 400
        Argent.center_y = 375

        self.list_items = arcade.SpriteList()
        self.list_items.append(Argent)
        self.list_items.append(potion_vie)

        # Background

        Background = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "church.webp"), scale = 1.3)
        Background.center_x = 300
        Background.center_y = 300

        self.background_list = arcade.SpriteList()
        self.background_list.append(Background)


        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=2, vertical_spacing=0, horizontal_spacing=0)

        #Items Shop
        self.stat_vie = GetLife()

        # Prix Shop
        self.prix_vie = self.stat_vie + 50

        # Boutons du menu
        self.life_button = arcade.gui.UIFlatButton(text="Life", width=100, height=50)
        self.coins_button = arcade.gui.UIFlatButton(text="Coins", width=100, height=50)

        # Ajouter la grille au manager avec un layout d'ancrage

        anchor_buy = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy.add(child = self.life_button, align_x=-100, align_y=-40)

        anchor_buy = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy.add(child = self.coins_button, align_x=+100, align_y=-40)


        @self.life_button.event("on_click")
        def on_click_life_button(event):
            """
            Description:
                Donne une récompense de vie et retourne à la carte.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.life_button.text = "Life"
            self.player.heal(self.stat_vie/4)
            from Map import Map
            Map_view = Map(self.player, self.compteur_maps, self.cleared_lvls)
            self.window.show_view(Map_view)

        @self.coins_button.event("on_click")
        def on_click_coins_button(event):
            """
            Description:
                Donne des pièces et retourne à la carte.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.coins_button.text = "Coins"
            AddArgent(100 + self.compteur_maps*2)
            from Map import Map
            Map_view = Map(self.player, self.compteur_maps, self.cleared_lvls)
            self.window.show_view(Map_view)

    def on_update(self,delta_time):
        """
        Description:
            Met à jour la vue de statue.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        pass


    def on_draw(self):
        """
        Description:
            Dessine la vue de statue et les récompenses.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.clear()
        self.background_list.draw()
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.draw()
        self.list_items.draw()
        arcade.draw_text("Portefeuille : " + str(GetArgent()),70,550, arcade.csscolor.WHITE,17)

    def on_show_view(self):
        """
        Description:
            Active la vue de statue.
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

# Main application setup
if __name__ == "__main__":
    window = arcade.Window(600, 600, "bonus_statue")
    statue_view = StatueView(1,player(), 1)
    window.show_view(statue_view)
    arcade.run()