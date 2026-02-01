"""
Description:
    Exemple simple de gestion des entrées clavier avec Arcade.
Entrées:
    Aucune.
Sorties:
    Aucune.
"""

import arcade


def on_key_press(key, modifiers):
    """
    Description:
        Affiche la touche pressée.
    Entrées:
        key: touche pressée.
        modifiers: modificateurs.
    Sorties:
        Aucune.
    """
    print(f"Key {key} was pressed")


def on_key_release(key, modifiers):
    """
    Description:
        Affiche la touche relâchée.
    Entrées:
        key: touche relâchée.
        modifiers: modificateurs.
    Sorties:
        Aucune.
    """
    print(f"Key {key} was released")


arcade.open_window(800, 600, "User Input Example")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
arcade.finish_render()

arcade.on_key_press = on_key_press
arcade.on_key_release = on_key_release

arcade.run()