import arcade

window = arcade.Window(600,600,"Titre beau",False,False)

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        self.batch=arcade.shape_list.ShapeElementList()

        herbegauche = arcade.shape_list.create_rectangle_filled(0,0,400,1200,arcade.csscolor.GREEN)
        herbedroite = arcade.shape_list.create_rectangle_filled(600,0,400,1200,arcade.csscolor.GREEN)



        Trottoir1 = arcade.shape_list.create_line(201,0,201,1200,arcade.csscolor.BLACK)
        Trottoir2 = arcade.shape_list.create_line(399.5,0,399.5,1200,arcade.csscolor.BLACK)


        self.batch.append(herbegauche)
        self.batch.append(herbedroite)
        self.batch.append(Trottoir1)
        self.batch.append(Trottoir2)




    def on_draw(self):
        self.clear()

        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)
        """
        texture = arcade.load_texture(os.path.join(os.path.dirname(__file__), "..", "Images", "Arbre.png"))
        scale = .3
        arcade.draw_texture_rect(texture,arcade.XYWH(80, 300, texture.width, texture.height).scale(scale))
        arcade.draw_texture_rect(texture,arcade.XYWH(530, 500, texture.width, texture.height).scale(scale))
        """

        self.batch.draw()




game = GameView()

window.show_view(game)
arcade.run()