import turtle

width = 500
height = 500
screen = turtle.Screen()
screen.setup(width,height,0,0)

def draw_koch_segment(t,ln):
    ln_part = 6
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
t.setpos(-240,-240)
t.hideturtle()
t.clear()
t.speed(500)


draw_koch_segment(t, 150)
t.left(60)
draw_koch_segment(t, 150)
t.left(60)
draw_koch_segment(t, 150)

turtle.done()