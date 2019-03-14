import arcade
from math import sin, cos, pi

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Hero:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.r = 20
        self.dir = 0
        self.color = arcade.color.RED

    def dx(self):
        return sin(self.dir * pi / 180)

    def dy(self):
        return cos(self.dir * pi / 180)

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)
        arcade.draw_line(self.x, self.y, self.x + 25 * self.dx(), self.y + 25 * self.dy(), [0, 0, 0], 3)

    def turn_left(self):
        self.dir -= 5

    def turn_right(self):
        self.dir += 5

    def move(self):
        self.x += self.dx()
        self.y += self.dy()

    def move_center(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def setup(self):
        # Настроить игру здесь
        self.hero = Hero()
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        # Здесь код рисунка
        self.hero.draw()

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        # self.hero.turn_right()
        self.hero.move()
        pass

    def on_key_press(self, key, modifiers):
        """Вызывается при нажатии пользователем клавиши"""
        if key == arcade.key.LEFT:
            self.hero.turn_left()
        elif key == arcade.key.RIGHT:
            self.hero.turn_right()
        elif key == arcade.key.SPACE:
            self.hero.move_center()



def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()