import arcade
import arcade.gui
from arcade.gui import UIManager
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
global multiplier
multiplier = 1
global button_click
global score
global upgrade


class MyFlatButton(arcade.gui.UIFlatButton):
    button_click = None

    def __init__(self, text: str, **kwargs):
        super().__init__(text, **kwargs)

    """
    To capture a button click, subclass the button and override on_click.
    """

    def on_click(self):
        """ Called when user lets off button """
        global button_click
        global multiplier
        global score
        button_click = True
        upgrade_button = 10

        if score - upgrade_button > 0:
            print('almost there')
            if button_click:
                print('success')
                score -= multiplier
                multiplier += 1

                button_click = False
                score -= upgrade_button
                upgrade_button += 1


class GameView(arcade.View):

    def __init__(self):
        global score

        super().__init__()
        self.ui_manager = UIManager()
        self.window.set_mouse_visible(True)

        arcade.set_background_color(arcade.color.RED)
        score = 0
        self.score_text = None

    def setup(self):
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        ui_input_box = arcade.gui.UIInputBox(
            center_x=left_column_x,
            center_y=y_slot * 2,
            width=300
        )
        button = MyFlatButton(
            'UPGRADE',
            center_x=right_column_x,
            center_y=y_slot * 1,
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(button)

    def on_draw(self):
        global score
        arcade.start_render()

        global multiplier

        output = f"Score: {score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_mouse_press(self, x, y, button, modifiers):
        global score
        global multiplier

        arcade.set_background_color([random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)])

        score += multiplier


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pog")
    window.show_view(GameView())
    arcade.run()


main()