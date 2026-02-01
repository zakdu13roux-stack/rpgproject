"""
Description:
    Menu principal du jeu avec options et réglage du volume.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import arcade
import arcade.gui
from PlayerStats import*
from Spawn import*

class MenuView(arcade.View):
    def __init__(self):
        """
        Description:
            Initialise le menu principal.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        super().__init__()
        self.manager = arcade.gui.UIManager()

        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=1, vertical_spacing=0, horizontal_spacing=0)

        # Boutons du menu
        resume_button = arcade.gui.UIFlatButton(text="Return to Game", width=200, height=50)
        options_button = arcade.gui.UIFlatButton(text="Options", width=200, height=50)
        """
        exit_button = arcade.gui.UIFlatButton(text="Exit", width=200, height=50)
        """

        # Ajouter les boutons à la grille
        self.grid.add(options_button, col_num=0, row_num=0)
        self.grid.add(resume_button, col_num=1, row_num=1)
        """
        self.grid.add(exit_button, col_num=0, row_num=2)
        """

        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="center", anchor_y="center")


        #commandes
        self.text_Z = arcade.create_text_sprite(("Up : Z"),arcade.csscolor.WHITE,15)
        self.text_S = arcade.create_text_sprite(("Down : S "),arcade.csscolor.WHITE,15)
        self.text_Q = arcade.create_text_sprite(("Left : Q"),arcade.csscolor.WHITE,15)
        self.text_D = arcade.create_text_sprite(("Right : D"),arcade.csscolor.WHITE,15)
        self.text_Portal = arcade.create_text_sprite(("Walk toward portal to teleport to map (Can't go back to spawn until you die)."),arcade.csscolor.WHITE,13)
        self.text_Shop = arcade.create_text_sprite(("Walk toward Shop to buy items and get better stats. "),arcade.csscolor.WHITE,13)
        self.text_Z.center_x = 55
        self.text_Z.center_y = 570
        self.text_S.center_x = 68
        self.text_S.center_y = 540
        self.text_Q.center_x = 60
        self.text_Q.center_y = 510
        self.text_D.center_x = 65
        self.text_D.center_y = 480
        self.text_Portal.center_x = 295
        self.text_Portal.center_y = 420
        self.text_Shop.center_x = 211
        self.text_Shop.center_y = 390
        self.texts = arcade.SpriteList()
        self.texts.append(self.text_Z)
        self.texts.append(self.text_S)
        self.texts.append(self.text_Q)
        self.texts.append(self.text_D)
        self.texts.append(self.text_Shop)
        self.texts.append(self.text_Portal)

        @resume_button.event("on_click")
        def on_click_resume_button(event):
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

        @options_button.event("on_click")
        def on_click_option_button(event):
            """
            Description:
                Ouvre la vue des options.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            option_view = Options()
            self.window.show_view(option_view)
        """
        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()
        """

    def on_draw(self):
        """
        Description:
            Dessine le menu principal.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.clear()
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
        self.manager.draw()
        self.texts.draw()

    def on_show_view(self):
        """
        Description:
            Active la vue du menu.
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

class Options(arcade.View):
    def __init__(self):
        """
        Description:
            Initialise la vue des options.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        super().__init__()
        self.manager = arcade.gui.UIManager()

        self.grille = arcade.gui.UIGridLayout(columns=1,vertical_spacing=0,horizontal_spacing=0)

        return_button = arcade.gui.UIFlatButton(text="Return",width=100,height=50)
        return_button.center_x=0
        return_button.center_y=0

        self.volume_button = arcade.gui.UIFlatButton(text="Volume", width=80, height=50)
        anchor_volume = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_volume.add(child=self.volume_button,align_x=0,align_y=0)

        @self.volume_button.event("on_click")
        def on_click_volume_button(event):
            """
            Description:
                Ouvre la vue de volume.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            volume_vue = VolumeView()
            self.window.show_view(volume_vue)


        self.grille.add(return_button,0,0)

        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grille, anchor_x="left", anchor_y="bottom")





        @return_button.event("on_click")
        def on_click_return_button(event):
            """
            Description:
                Retourne au menu principal.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            vue_menu = MenuView()
            self.window.show_view(vue_menu)



    def on_draw(self):
        """
        Description:
            Dessine la vue des options.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.clear()
        self.manager.draw()


    def on_show_view(self):
        """
        Description:
            Active la vue des options.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
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

class VolumeView(arcade.View):
    def __init__(self):
        """
        Description:
            Initialise la vue de réglage du volume.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        super().__init__()
        self.manager = arcade.gui.UIManager()

        return_button = arcade.gui.UIFlatButton(text="Return",width=100,height=50)

        self.grille = arcade.gui.UIGridLayout(columns=1,vertical_spacing=0,horizontal_spacing=0)

        @return_button.event("on_click")
        def on_click_return_button(event):
            """
            Description:
                Retourne à la vue des options.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            vue_option = Options()
            self.window.show_view(vue_option)

        self.grille.add(return_button,0,0)

        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grille, anchor_x="left", anchor_y="bottom")








        self.v1_button = arcade.gui.UIFlatButton(text="+1", width=80, height=50)
        self.v2_button = arcade.gui.UIFlatButton(text="-1", width=80, height=50)



        anchor_volumes = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_volumes.add(child=self.v1_button,align_x=50,align_y=50)
        anchor_volumes.add(child=self.v2_button,align_x=-50,align_y=50)

        @self.v1_button.event("on_click")
        def on_click_return_button(event):
            """
            Description:
                Augmente le volume.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            if GetVolume() <1.0:
                ChangeVolume(GetVolume()+0.1)

        @self.v2_button.event("on_click")
        def on_click_return_button(event):
            """
            Description:
                Diminue le volume.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            if GetVolume() >0.0:
                ChangeVolume(GetVolume()-0.1)

    def on_draw(self):
        """
        Description:
            Dessine la vue de réglage du volume.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        self.clear()
        self.manager.draw()
        arcade.draw_text("Volume Actuel : " + str(GetVolume()),200,300, arcade.csscolor.RED,17)


    def on_update(self,delta_time):
        """
        Description:
            Met à jour la vue de volume.
        Entrées:
            delta_time: pas de temps.
        Sorties:
            Aucune.
        """
        pass





    def on_show_view(self):
        """
        Description:
            Active la vue de volume.
        Entrées:
            Aucune.
        Sorties:
            Aucune.
        """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
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
    window = arcade.Window(600, 600, "RPG Game with Menu")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()