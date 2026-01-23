import arcade
import arcade.gui

from Spawn import*

class MenuView(arcade.View):
    def __init__(self,compteur_maps):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        self.compteur_maps = compteur_maps

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


        @resume_button.event("on_click")
        def on_click_resume_button(event):
            spawn_view = Spawn(self.compteur_maps)
            self.window.show_view(spawn_view)

        @options_button.event("on_click")
        def on_click_option_button(event):
            option_view = Options(self.compteur_maps)
            self.window.show_view(option_view)
        """
        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()
        """

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
        self.manager.draw()

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.GREEN)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

class Options(arcade.View):
    def __init__(self,compteur_maps):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        self.grille = arcade.gui.UIGridLayout(columns=1,vertical_spacing=0,horizontal_spacing=0)

        self.compteur_maps = compteur_maps


        return_button = arcade.gui.UIFlatButton(text="Return",width=100,height=50)
        return_button.center_x=0
        return_button.center_y=0

        self.grille.add(return_button,0,0)

        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grille, anchor_x="left", anchor_y="bottom")

        self.WIP = arcade.create_text_sprite("Work In Progress", arcade.csscolor.RED, 50)
        self.WIP.center_x = 300
        self.WIP.center_y = 300

        self.text_list = arcade.SpriteList()

        self.text_list.append(self.WIP)



        @return_button.event("on_click")
        def on_click_return_button(event):
            vue_menu = MenuView(self.compteur_maps)
            self.window.show_view(vue_menu)

    def on_draw(self):
        self.clear()
        self.text_list.draw()
        self.manager.draw()


    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

# Main application setup
if __name__ == "__main__":
    window = arcade.Window(600, 600, "RPG Game with Menu")
    menu_view = MenuView(1)
    window.show_view(menu_view)
    arcade.run()