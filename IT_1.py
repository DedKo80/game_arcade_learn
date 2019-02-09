import random
import arcade

# constants def
SCREEN_WIDTH = 810
SCREEN_HEIGHT = 840
CELL_SIZE = 30
SCREEN_COLOR = arcade.color.WHITE
CELL_LINE_COLOR = arcade.color.GRAY_BLUE
COLOR_RED = arcade.color.RED


def to_screen_cooord(x=1, y=1):
    return [x * CELL_SIZE, y * CELL_SIZE]


# рисуем тетрадь в клетку
def draw_cells():
    for i in range(SCREEN_HEIGHT // CELL_SIZE):
        arcade.draw_line(0, i * CELL_SIZE, SCREEN_WIDTH, i * CELL_SIZE, CELL_LINE_COLOR)
    for j in range(SCREEN_WIDTH // CELL_SIZE):
        if j == SCREEN_WIDTH // CELL_SIZE - 4:
            tmp_color = COLOR_RED
            tmp_size = 4
        else:
            tmp_color = CELL_LINE_COLOR
            tmp_size = 1
        arcade.draw_line(j * CELL_SIZE, 0, j * CELL_SIZE, SCREEN_HEIGHT, tmp_color, tmp_size)


# рисуем крестик
def draw_cross(x, y):
    dl = CELL_SIZE // 2
    x = x * CELL_SIZE + CELL_SIZE // 2
    y = y * CELL_SIZE + CELL_SIZE // 2
    arcade.draw_line(x - dl, y + dl, x + dl, y - dl, COLOR_RED, 5)
    arcade.draw_line(x + dl, y + dl, x - dl, y - dl, COLOR_RED, 5)


# рисуем нолик
def draw_null(x, y):
    dl = CELL_SIZE // 2
    y = y * CELL_SIZE + CELL_SIZE // 2 - CELL_SIZE // 10
    x = x * CELL_SIZE + CELL_SIZE // 2 - CELL_SIZE // 10
    arcade.draw_circle_outline(x, y , dl, COLOR_RED, 2)


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Title window')
arcade.set_background_color(SCREEN_COLOR)

arcade.start_render()
draw_cells()
arcade.draw_circle_outline(*to_screen_cooord(6, 8), CELL_SIZE * 2, COLOR_RED, 3)

for i in range(3):
    for j in range(3):
        if random.randint(0, 1) == 0:
            draw_cross(i, j)
        else:
            draw_null(i, j)

arcade.finish_render()

arcade.run()