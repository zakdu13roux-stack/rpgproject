"""
Description:
    Vue boutique pour acheter des améliorations et revenir au spawn.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import arcade
import arcade.gui
from Spawn import Spawn
from PlayerStats import *

class ShopView(arcade.View):
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

        #Sprites
        potion_vie = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "potionverte.png"), scale = 0.167)
        potion_vie.center_x=150
        potion_vie.center_y= 385

        self.epee_black = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "epeeblack.png"), scale = 0.15)
        self.epee_black.center_x = 415
        self.epee_black.center_y = 385

        self.list_items = arcade.SpriteList()
        self.list_items.append(potion_vie)
        self.list_items.append(self.epee_black)


        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=2, vertical_spacing=0, horizontal_spacing=0)

        #Items Shop
        self.stat_vie = GetLife()

        # Prix Shop
        self.prix_vie = self.stat_vie + 50


        # Boutons du menu
        return_button = arcade.gui.UIFlatButton(text="Return", width=200, height=50)
        self.buy_life_button = arcade.gui.UIFlatButton(text=str(self.prix_vie), width=100, height=50)
        self.buy_weapon_button = arcade.gui.UIFlatButton(text="Better Weapons", width=150, height=50)

        # Ajouter les boutons à la grille
        self.grid.add(return_button, col_num=1, row_num=0)


        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        anchor.add(child=self.grid, anchor_x="left", anchor_y="bottom")

        anchor_buy_life = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy_life.add(child = self.buy_life_button, align_x=-150, align_y=0)

        anchor_buy_weapon = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy_weapon.add(child = self.buy_weapon_button, align_x=125, align_y=0)


        @self.buy_life_button.event("on_click")
        def on_click_buy_button(event):
            """
            Description:
                Achète l'amélioration si possible.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.buy_life_button.text = str(self.prix_vie)
            if self.prix_vie<=GetArgent():
                AddLife(50)
                AddArgent(-int(self.prix_vie))
                self.prix_vie = GetLife() +50

        @self.buy_weapon_button.event("on_click")
        def on_click_buy_weapon_button(event):
            """
            Description:
                Achète l'amélioration si possible.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.buy_weapon_button.text = ""
            weapon_shop = WeaponShop()
            self.window.show_view(weapon_shop)


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
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.draw()
        self.list_items.draw()
        arcade.draw_text("Portefeuille : " + str(GetArgent()),70,570, arcade.csscolor.BLACK,17)

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


class WeaponShop(arcade.View):
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

        #Sprites
        branche = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "branche.png"), scale = 0.35)
        branche.center_x= 125
        branche.center_y= 470

        banana = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "banane.png"), scale = 0.17)
        banana.center_x= 295
        banana.center_y= 470

        H2F = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "H2F.png"), scale = 0.15)
        H2F.center_x= 450
        H2F.center_y= 485

        spear = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "lance.png"), scale = 0.22)
        spear.center_x= 240
        spear.center_y= 270

        epeeRouillee = arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "epee rouillee.png"), scale = 0.15)
        epeeRouillee.center_x= 380
        epeeRouillee.center_y= 270

        self.list_items = arcade.SpriteList()
        self.list_items.append(branche)
        self.list_items.append(banana)
        self.list_items.append(H2F)
        self.list_items.append(spear)
        self.list_items.append(epeeRouillee)


        # Grille pour organiser les boutons
        self.grid = arcade.gui.UIGridLayout(columns=2, vertical_spacing=0, horizontal_spacing=0)

        #Items Shop
        self.stat_vie = GetLife()

        # Prix Shop
        self.prix_vie = self.stat_vie + 50


        # Boutons du menu
        return_button = arcade.gui.UIFlatButton(text="Return", width=200, height=50)
        self.buy_branche_button = arcade.gui.UIFlatButton(text="Stick (free)", width=120, height=50)
        self.buy_banana_button = arcade.gui.UIFlatButton(text="Banana (75)", width=120, height=50)
        self.buy_H2F_button = arcade.gui.UIFlatButton(text="Iron Axe (1420)", width=120, height=50)
        self.buy_epee_rouillee_button = arcade.gui.UIFlatButton(text="Sword (350)", width=120, height=50)
        self.buy_lance_button = arcade.gui.UIFlatButton(text="Spear (670)", width=120, height=50)

        # Ajouter les boutons à la grille
        self.grid.add(return_button, col_num=1, row_num=0)


        # Ajouter la grille au manager avec un layout d'ancrage
        anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor.add(child=self.grid, anchor_x="left", anchor_y="bottom")

        anchor_buy_branche = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy_branche.add(child = self.buy_branche_button, align_x=-170, align_y=100)

        anchor_buy_banana = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy_banana.add(child = self.buy_banana_button, align_x=-10, align_y=100)

        anchor_buy_H2F = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy_H2F.add(child = self.buy_H2F_button, align_x=150, align_y=100)

        anchor_buy_lance = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy_lance.add(child = self.buy_lance_button, align_x=-75, align_y=-100)

        anchor_buy_epee_rouillee = self.manager.add(arcade.gui.UIAnchorLayout())
        anchor_buy_epee_rouillee.add(child = self.buy_epee_rouillee_button, align_x=75, align_y=-100)



        @self.buy_branche_button.event("on_click")
        def on_click_buy_branche_button(event):
            """
            Description:
                Achète l'amélioration si possible.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.buy_branche_button.text = "Stick (free)"
            item = GetItems()
            for x in range(3):
                for y in range(2):
                    if item[y][x] == 0:
                        GiveItem(1,x,y)
                        return


        @self.buy_banana_button.event("on_click")
        def on_click_buy_banana_button(event):
            """
            Description:
                Achète l'amélioration si possible.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.buy_banana_button.text = "Banana (75)"
            if GetArgent() > 75:
                item = GetItems()
                for x in range(3):
                    for y in range(2):
                        if item[y][x] == 0:
                            GiveItem(2,x,y)
                            AddArgent(-75)
                            return


        @self.buy_H2F_button.event("on_click")
        def on_click_buy_H2F_button(event):
            """
            Description:
                Achète l'amélioration si possible.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.buy_H2F_button.text = "Iron Axe (1420)"
            if GetArgent() > 1000:
                item = GetItems()
                for x in range(3):
                    for y in range(2):
                        if item[0][x] == 0 and item[1][x] == 0:
                            GiveItem(3,x,y)
                            AddArgent(-1420)
                            return

        @self.buy_epee_rouillee_button.event("on_click")
        def on_click_buy_epee_rouillee_button(event):
            """
            Description:
                Achète l'amélioration si possible.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.buy_epee_rouillee_button.text = "Sword (350)"
            if GetArgent() > 100:
                item = GetItems()
                for x in range(3):
                    for y in range(2):
                        if item[y][x] == 0:
                            GiveItem(4,x,y)
                            AddArgent(-350)
                            return

        @self.buy_lance_button.event("on_click")
        def on_click_buy_lance_button(event):
            """
            Description:
                Achète l'amélioration si possible.
            Entrées:
                event: événement de clic.
            Sorties:
                Aucune.
            """
            self.buy_lance_button.text = "Spear (670)"
            if GetArgent() > 100:
                item = GetItems()
                for x in range(3):
                    for y in range(2):
                        if item[y][x] == 0:
                            GiveItem(5,x,y)
                            AddArgent(-670)
                            return

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
            shop_view = ShopView()
            self.window.show_view(shop_view)

        # Cartable
        self.sac()

    def sac(self):
        self.SacGraphique=arcade.SpriteList()
        self.SacItems=arcade.SpriteList()
        # Forme du sac
        self.SacStorage=GetItems()
        for h in range(len(self.SacStorage)):
            for l in range(len(self.SacStorage[0])):
                case=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "fond_sac.png"), scale=0.2)
                case.center_x=375+90*l
                case.center_y=40+85*h
                case.pos=f"{h}{l}"
                self.SacGraphique.append(case)
                if self.SacStorage[h][l]==1:
                    BrancheImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "branche.png"), scale=0.4)
                    BrancheImage.center_x=375+90*l
                    BrancheImage.center_y=45+85*h
                    self.SacItems.append(BrancheImage)
                elif self.SacStorage[h][l]==2:
                    BananeImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "banane.png"), scale=0.2)
                    BananeImage.center_x=375+90*l
                    BananeImage.center_y=45+85*h
                    self.SacItems.append(BananeImage)
                elif self.SacStorage[0][l]==3:
                    H2FImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "H2F.png"), scale=0.225)
                    H2FImage.center_x=375+90*l
                    H2FImage.center_y=80
                    self.SacItems.append(H2FImage)
                elif self.SacStorage[h][l]==4:
                    EpeerouilleeImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "epee rouillee.png"), scale=0.15)
                    EpeerouilleeImage.center_x=375+90*l
                    EpeerouilleeImage.center_y=40+85*h
                    self.SacItems.append(EpeerouilleeImage)
                elif self.SacStorage[h][l]==5:
                    LanceImage=arcade.Sprite(os.path.join(os.path.dirname(__file__), "..", "Images", "lance.png"), scale=0.20)
                    LanceImage.center_x=375+90*l
                    LanceImage.center_y=40+85*h
                    self.SacItems.append(LanceImage)

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
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        self.manager.draw()
        self.list_items.draw()
        arcade.draw_text("Portefeuille : " + str(GetArgent()),70,570, arcade.csscolor.BLACK,17)
        self.SacGraphique.draw()
        self.SacStorage = GetItems()
        self.sac()
        self.SacItems.draw()

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

    def on_mouse_press(self, x, y, button, modifier):
        """
        Description:
            Gère la sélection de cible et l'utilisation d'objets.
        Entrées:
            x: position x de la souris.
            y: position y de la souris.
            button: bouton pressé.
            modifier: modificateurs.
        Sorties:
            Aucune.
        """
        if button == 1:
            ItemClicked=arcade.get_sprites_at_point((x,y),self.SacGraphique)
            if ItemClicked!=[]:
                if self.SacStorage[int(ItemClicked[0].pos[0])][int(ItemClicked[0].pos[1])] !=0:
                    GiveItem(0,int(ItemClicked[0].pos[1]),int(ItemClicked[0].pos[0]))



# Main application setup
if __name__ == "__main__":
    window = arcade.Window(600, 600, "RPG Game with Menu")
    menu_view = ShopView()
    window.show_view(menu_view)
    arcade.run()