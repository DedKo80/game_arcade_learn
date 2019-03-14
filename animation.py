import arcade
import random
from math import pi, cos, sin


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def get_distance(hero1, hero2):
    return ((hero1.x - hero2.x) ** 2 + (hero1.y - hero2.y) ** 2) ** 0.5

class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.speed = 3
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.color = [10, 10, 10]

    def draw(self):
        arcade.draw_line(self.x, self.y,
                         self.x + self.dx * 5,
                         self.y + self.dy * 5,
                         self.color, 4)

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def is_removeble(self):
        out_x = not 0 < self.x < SCREEN_WIDTH
        out_y = not 0 < self.y < SCREEN_HEIGHT
        return out_x or out_y

    def is_hit(self, hero):
        return get_distance(self, hero) <= hero.r

class Hero:
    def __init__(self, color=arcade.color.RED, size=30):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.dir = random.randint(0, 360)
        self.r = size
        self.speed = 1
        self.dx = sin(self.dir * pi / 180)
        self.dy = cos(self.dir * pi / 180)

        self.color = color

    def it_crach(self, hero):
        return get_distance(self, hero) <= self.r + hero.r

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

        if self.y > SCREEN_HEIGHT - self.r or self.y < self.r:
            self.dir = 180 - self.dir
            self.dx = sin(self.dir * pi / 180)
            self.dy = cos(self.dir * pi / 180)
        # print(self.dir, self.y)

        if self.x > SCREEN_WIDTH - self.r:
            self.x = SCREEN_WIDTH - self.r
        if self.x < self.r:
            self.x = self.r
        if self.y > SCREEN_HEIGHT - self.r:
            self.y = SCREEN_HEIGHT- self.r
        if self.y < self.r:
            self.y = self.r
            
        self.y += self.dy * self.speed
        self.x += self.dx * self.speed

    def speed_up(self):
        if 0 <= self.speed < 10:
            self.speed += 1

    def speed_down(self):
        if 1 <= self.speed <= 10:
            self.speed -= 1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)
        x1, y1, = self.x, self.y
        x2 = x1 + self.r * 1.3 * self.dx
        y2 = y1 + self.r * 1.3 * self.dy
        arcade.draw_line(x1, y1, x2, y2, arcade.color.BLACK, 4)

    def get_telemetry(self):
        st = 'x = {} \ny = {} \n'.format(self.x // 1, self.y // 1) + \
             'dir = {} \n'.format(self.dir) + \
             'speed = {} \n'.format(self.speed)

        return st


class MyGame(arcade.Window):
    """ Главный класс приложения. """
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color([240, 240, 240, 150])

    def setup(self):
        # Настроить игру здесь
        self.hero = Hero()
        self.enemy_list = []
        self.bullet_list = []
        for i in range(20):
            self.enemy_list.append(Hero(color=arcade.color.BLUE, size=10))

    def get_telemetry(self):
        st = 'x = {} \ny = {} \n'.format(self.hero.x // 1, self.hero.y // 1) + \
             'dir = {} \n'.format(self.hero.dir) + \
             'speed = {} \n'.format(self.hero.speed) + \
             'count bullets = {}\n'.format(len(self.bullet_list)) + \
             'count enemy = {}\n'.format(len(self.enemy_list))
        return st

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.hero.draw()
        for enemy in self.enemy_list:
            enemy.draw()
            arcade.draw_line(self.hero.x, self.hero.y, enemy.x, enemy.y, [50, 50, 50])
            arcade.draw_text(str(get_distance(self.hero, enemy) // 1), enemy.x + 20, enemy.y + 20, [90,90,90])
        for bullet in self.bullet_list:
            bullet.draw()
        arcade.draw_text(self.get_telemetry(), 10, 100, [0, 240, 0])
        # Здесь код рисунка

    def on_key_press(self, key, modifiers):
        """Вызывается при нажатии пользователем клавиши"""

        if key == arcade.key.MOTION_LEFT:
            self.hero.turn_left()
        elif key == arcade.key.MOTION_RIGHT:
            self.hero.turn_right()
        elif key == arcade.key.UP:
            self.hero.speed_up()
        elif key == arcade.key.DOWN:
            self.hero.speed_down()
        elif key == arcade.key.SPACE:
            self.bullet_list.append(Bullet(self.hero.x + self.hero.dx * self.hero.r,
                                           self.hero.y + self.hero.dy * self.hero.r,
                                           self.hero.dx, self.hero.dy))
        print(self.hero.speed)


    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        self.hero.move()
        for enemy in self.enemy_list:
            enemy.move()

        for bullet in self.bullet_list:
            bullet.move()
            if bullet.is_removeble():
                self.bullet_list.remove(bullet)
            for enemy in self.enemy_list:
                if bullet.is_hit(enemy):
                    self.bullet_list.remove(bullet)
                    self.enemy_list.remove(enemy)


        for enemy in self.enemy_list:
            if self.hero.it_crach(enemy):
                self.hero.r += 2
                self.enemy_list.remove(enemy)
            pass
            # self.hero.turn_right()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()