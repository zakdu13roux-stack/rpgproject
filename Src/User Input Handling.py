import arcade


def on_key_press(key, modifiers):
    print(f"Key {key} was pressed")


def on_key_release(key, modifiers):
    print(f"Key {key} was released")


arcade.open_window(800, 600, "User Input Example")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
arcade.finish_render()

arcade.on_key_press = on_key_press
arcade.on_key_release = on_key_release

arcade.run()