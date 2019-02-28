import arcade
from math import pi, cos, sin

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Hero:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.dir = 0
        self.r = 30
        self.dx = sin(self.dir * pi / 180)
        self.dy = cos(self.dir * pi / 180)

        self.color = arcade.color.RED


    def turn_left(self):
        self.dir -= 5
        self.dx = sin(self.dir * pi / 180)
        self.dy = cos(self.dir * pi / 180)

    def turn_right(self):
        self.dir += 5
        self.dx = sin(self.dir * pi / 180)
        self.dy = cos(self.dir * pi / 180)

    def move(self):
        if self.x > SCREEN_WIDTH - self.r or self.x < self.r:
            self.dir *= -1
            self.dx = sin(self.dir * pi / 180)
            self.dy = cos(self.dir * pi / 180)

        if self.y > SCREEN_HEIGHT - self.r and self.y < self.r:
            self.dir -= 180
            self.dx = sin(self.dir * pi / 180)
            self.dy = cos(self.dir * pi / 180)
        print(self.dir, self.y)

        self.y += self.dy
        self.x += self.dx

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)
        x1, y1, = self.x, self.y
        x2 = x1 + self.r * 1.3 * self.dx
        y2 = y1 + self.r * 1.3 * self.dy
        arcade.draw_line(x1, y1, x2, y2, arcade.color.BLACK, 4)

class MyGame(arcade.Window):
    """ Главный класс приложения. """
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color([240, 240, 240, 150])

    def setup(self):
        # Настроить игру здесь
        self.hero = Hero()
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.hero.draw()
        # Здесь код рисунка

    def on_key_press(self, key, modifiers):
        """Вызывается при нажатии пользователем клавиши"""

        if key == arcade.key.LEFT:
            self.hero.turn_left()
        elif key == arcade.key.RIGHT:
            self.hero.turn_right()
        elif key == arcade.key.UP:
            self.hero.move()


    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        self.hero.move()
        # self.hero.turn_right()
        pass


        # elif key == arcade.key.LEFT:
        #     self.player_sprite.change_x = -MOVEMENT_SPEED
        # elif key == arcade.key.RIGHT:
        #     self.player_sprite.change_x = MOVEMENT_SPEED


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()