import arcade
import random
from math import sin, cos, pi, acos

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.speed = 3
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.color = [10, 10, 10]

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 4, self.color)
         # arcade.draw_line(self.x, self.y,
         #                 self.x + self.dx * 5,
         #                 self.y + self.dy * 5,
         #                 self.color, 4)

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def is_removeble(self):
        out_x = not 0 < self.x < SCREEN_WIDTH
        out_y = not 0 < self.y < SCREEN_HEIGHT
        return out_x or out_y


class Hero:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.speed = 0
        self.dir = 0
        self.dx = cos(self.dir * pi / 180)
        self.dy = sin(self.dir * pi / 180)
        self.r = 30
        self.color = [200, 0, 0]

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)
        arcade.draw_line(self.x, self.y,
                         self.x + 1.2 * self.r * self.dx, self.y + 1.2 * self.r * self.dy,
                         [20, 20, 20], 3)

    def turn_to(self, x, y):
        dx = x - self.x
        dy = y - self.y
        dr = (dx ** 2 + dy ** 2) ** 0.5
        self.dir = acos(dx / dr) * 180 / pi
        if dy < 0:
            self.dir *= -1
        self.dx = cos(self.dir * pi / 180)
        self.dy = sin(self.dir * pi / 180)

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed


class MyGame(arcade.Window):
    """ Главный класс приложения. """
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.hero = Hero()
        self.bullet_list = []

    def setup(self):
        # Настроить игру здесь
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.hero.draw()
        for bullet in self.bullet_list:
            bullet.draw()
        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        self.hero.move()
        for bullet in self.bullet_list:
            bullet.move()
            if bullet.is_removeble():
                self.bullet_list.remove(bullet)
                pass
        print(len(self.bullet_list))

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.UP:
            self.hero.move()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.hero.speed = 2
        elif button == arcade.MOUSE_BUTTON_LEFT:
            self.bullet_list.append(Bullet(self.hero.x, self.hero.y, self.hero.dx, self.hero.dy))

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.hero.speed = 0

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.hero.turn_to(x, y)
        # print(self.hero.dir)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()