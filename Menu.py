import arcade
import arcade.gui

from Spawn import Spawn

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()

        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=1, vertical_spacing=0, horizontal_spacing=0)

        # Boutons du menu
        resume_button = arcade.gui.UIFlatButton(text="Resume", width=200, height=50)
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
            spawn_view = Spawn()
            self.window.show_view(spawn_view)
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

# Main application setup
if __name__ == "__main__":
    window = arcade.Window(600, 600, "RPG Game with Menu")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()