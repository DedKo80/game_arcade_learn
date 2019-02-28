import arcade
import random
from math import cos, sin, pi

# constants def
SCREEN_WIDTH = 810
SCREEN_HEIGHT = 840
SCREEN_COLOR = arcade.color.WHITE
COLOR_RED = arcade.color.RED

# x = 100
# y = 100
# ang = 0

class Ball:
    def __init__(self):
        self.x = random.randint(10, SCREEN_WIDTH - 10)
        self.y = random.randint(10, SCREEN_WIDTH - 10)
        self.r = random.randint(10, 50)
        self.color = arcade.color.RED

    def draw(self):
        arcade.draw_point(self.x, self.y, self.color, self.r)

    def move(self):
        self.x = random.randint(10, SCREEN_WIDTH - 10)
        self.y = random.randint(10, SCREEN_WIDTH - 10)

    def update(self):
        self.move()
        # self.draw()


def on_draw(dt):
    arcade.start_render()
    arcade.draw_point(100, 100, COLOR_RED, 30)

def upd(bl):
    bl.draw

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Animation')
    arcade.set_background_color(SCREEN_COLOR)

    ball = Ball()
    print(ball.x, ball.color)
    ball.move()
    arcade.start_render()

    arcade.schedule(upd(ball), 1 / 2)
    arcade.run()

if __name__ == '__main__':
    main()