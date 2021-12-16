"""
Platform game
https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html
"""

import arcade
import typing

# constants
SCREEN_WIDTH = 1000
SCREEEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"
RESIZABLE = True


class MyGame(arcade.Window):
    "Main application class"

    def __init__(self) -> None:
        
        # call parent class and set up window
        super().__init__(SCREEN_WIDTH, SCREEEN_HEIGHT, SCREEN_TITLE, resizable=RESIZABLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen """
        arcade.start_render()

        # add some code to draw the screen 

def main():
    """Main function."""
    window = MyGame()
    window.setup()
    window.run()

if __name__ == "__main__":
    main()