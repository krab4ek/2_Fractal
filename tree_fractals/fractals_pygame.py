import os
import pygame
import random

from turtle_pygame import TurtlePygame
from l_system_2d import LSystem2D


# список функций для управления параметаризированными командами
# у всех функций будет префикс cmd_ и первый параметр t - черепашка
def cmd_turtle_fd(t, length, *args):
    t.pensize(args[1])
    t.pencolor((48, 34, 26))
    t.fd(length*args[0])
    t.pencolor((0, 0, 0))

def cmd_turtle_left(t, angle, *args):
    t.left(args[0])

def cmd_turtle_right(t, angle, *args):
    t.right(args[0])

def cmd_turtle_leaf(t, length, *args):
    if random.random() > 0.2:       # вероятность рисования листа
        return

    p = t.pensize()
    t.pensize(5)
    p = random.randint(0, 2)
    if p == 0:
        t.pencolor((0, 153, 0))
    elif p == 1:
        t.pencolor((102, 121, 0))
    else:
        t.pencolor((32, 187, 0))

    t.fd(length//2)
    t.pencolor((0, 0, 0))
    t.pensize(p)

# ----------  чтобы окно появлялось в верхнем левом углу ------------
x = 20
y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
# --------------------------------------------------------------------

pygame.init()

W = 1200
H = 600

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Черепашка")

WHITE = (255, 255, 255)

FPS = 30        # число кадров в секунду
clock = pygame.time.Clock()

surf = pygame.Surface((W, H))
surf.fill(WHITE)

t = TurtlePygame(surf)

pen_width = 2   # толщина линии рисования (в пикселах)
f_len = 20      # длина одного сегмента прямой (в пикселах)
angle = 20

axiom = "A"

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)

l_sys.add_rules(("A", f"F(1, 1)[+({angle})A][-({angle})A]", 0.5),
                ("A", f"F(1, 1)[++({angle})A][+({angle})A][-({angle})A][--({angle})A]", 0.4),
                ("A", f"F(1, 1)[-({angle})A]", 0.05),
                ("A", f"F(1, 1)[+({angle})A]", 0.05),

                ("F(x, y)", lambda x, y: f"F({(1.2+random.triangular(-0.2, 0.2, random.gauss(0, 0.5)))*x}, {1.4*y})"),
                ("+(x)", lambda x: f"+({x + random.triangular(-10, 10, random.gauss(0, 2))})"),
                ("-(x)", lambda x: f"-({x + random.triangular(-10, 10, random.gauss(0, 2))})"),
                )

l_sys.add_rules_move(("F", cmd_turtle_fd), ("+", cmd_turtle_left), ("-", cmd_turtle_right),
                     ("A", cmd_turtle_leaf))
#print(l_sys.state)

n = 1
step = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if step > FPS and n < 4:
        step = 0
        n += 1
        l_sys.generate_path(n)
        surf.fill(WHITE)
        l_sys.draw_turtle((W // 2, H-20), 90)

    step += 1

    sc.blit(surf, (0, 0))
    pygame.display.update()

    clock.tick(FPS)
