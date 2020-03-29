# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150
CENTER_W = SCREEN_WIDTH / 2
CENTER_H = SCREEN_HEIGHT / 2

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

# Clear the screen and start drawing
arcade.start_render()

# Draw a blue circle
arcade.draw_circle_filled(
    CENTER_W, CENTER_H, RADIUS, arcade.color.YELLOW
)

arcade.draw_circle_filled(
    CENTER_W - RADIUS/2, CENTER_H + RADIUS/2, RADIUS/2/3, arcade.color.BABY_BLUE)

arcade.draw_circle_filled(
    CENTER_W + RADIUS/2, CENTER_H + RADIUS/2, RADIUS/2/3, arcade.color.BABY_BLUE)

arcade.draw_arc_outline(CENTER_W, CENTER_H - RADIUS/3/2,
                        200, 200, arcade.color.RED, 180+30, 360-30, 40)

# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()
