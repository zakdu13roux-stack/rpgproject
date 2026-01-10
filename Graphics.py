import arcade



arcade.open_window(600,600,"Main Fenêtre",False,True)

arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

arcade.start_render()


#Carrés d'herbe
arcade.draw_rect_filled(arcade.rect.XYWH(0,0,400,1200),arcade.csscolor.GREEN)
arcade.draw_rect_filled(arcade.rect.XYWH(600,0,400,1200),arcade.csscolor.GREEN)

#Arbres
texture = arcade.load_texture("Images/Arbre.png")
scale = .3
arcade.draw_texture_rect(texture,arcade.XYWH(80, 300, texture.width, texture.height).scale(scale))
arcade.draw_texture_rect(texture,arcade.XYWH(530, 500, texture.width, texture.height).scale(scale))


#Troittoirs
arcade.draw_line(201,0,201,1200,arcade.csscolor.BLACK)
arcade.draw_line(399.5,0,399.5,1200,arcade.csscolor.BLACK)


arcade.finish_render()

arcade.run()
