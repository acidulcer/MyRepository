from turtle import Turtle
default_scale = 10

def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)

def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale

def test_drawman():
    """
    Тестирование работы Чертежника
    :return: None
    """
    pen_down()
    for i in range(5):
        on_vector(10,20)
        on_vector(0, -20)
    pen_up()
    to_point(0,0)



def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)



def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)

def drawman_draw_grid(color_grid):
    """
    рисует кооринтаную сетку без осей
    запоминает размер окна поля
    x_width - ширина окна поля в пикселах
    y_height - высота окна поля в пикселах
    :param color_grid: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :return:
    """
    x_width = t.screen.window_width()
    y_height = t.screen.window_height()
    drawman_draw_Hline(x_width, y_height, color_grid)
    drawman_draw_Vline(x_width, y_height, color_grid)
    pen_up()
    to_point(0, 0)

def drawman_draw_Vline(x_width, y_height, color):
    """
    ВАРИАНТ 1: линии начинает рисовать с нижнего левого угла поля

    рисует вертикальные линии сетки, учитывая масштабирование Четрежника

    :param color: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :param x_width: ширина окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :param y_height: высота окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :return:
    """
    y = -y_height//2
    x = -x_width//2
    while x <= x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, y_height//2)
        t.penup()
        x = x + x_width//_drawman_scale


def drawman_draw_Hline(x_width, y_height, color):
    """
    ВАРИАНТ 1: линии начинает рисовать с нижнего левого угла поля

    рисует горизонтальные линии сетки, учитывая масштабирование Четрежника

    :param color: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :param x_width: ширина окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :param y_height: высота окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    """
    y = -y_height//2
    x = -x_width//2
    while y <= y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x_width//2, y)
        t.penup()
        y = y + y_height//_drawman_scale


init_drawman()
if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(2)