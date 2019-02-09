import arcade

# constants def
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
CELL_SIZE = 30
SCREEN_COLOR = arcade.color.WHITE
CELL_LINE_COLOR = arcade.color.GRAY_BLUE
COLOR_RED = arcade.color.RED


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


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Title window')
arcade.set_background_color(SCREEN_COLOR)

arcade.start_render()
draw_cells()
arcade.draw_circle_outline(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                           CELL_SIZE * 2, COLOR_RED, 3)




arcade.finish_render()

arcade.run()