import turtle

width = 1280
height = 720
screen = turtle.Screen()
screen.setup(width,height,0,0)

def draw_koch_segment(t,ln):
    ln_part = 8
    if ln > ln_part:
        ln_part = ln//3
        draw_koch_segment(t,ln_part)
        t.left(60)
        draw_koch_segment(t, ln_part)
        t.right(120)
        draw_koch_segment(t,ln_part)
        t.left(60)
        draw_koch_segment(t,ln_part)
            
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t .fd(ln)

t = turtle.Turtle()
t.speed(100)
t.ht()
draw_koch_segment(t, 1000)

turtle.done()