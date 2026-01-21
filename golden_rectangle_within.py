import turtle

def golden_rect_spiral(n=10, scale=5):
    fib = [1,1]
    for _ in range(n): fib.append(fib[-1]+fib[-2])

    t = turtle.Turtle()
    t.speed(0)
    turtle.bgcolor("navy")
    t.pencolor("gold")
    t.pensize(3)

    for i in range(1, len(fib)):
        side = fib[i] * scale

        # rectangle
        t.fillcolor("gold" if i%2 else "#ffd700")
        t.begin_fill()
        for _ in range(2):
            t.forward(side)
            t.left(90)
            t.forward(fib[i-1] * scale)
            t.left(90)
        t.end_fill()

        t.forward(side)
        t.left(90)

    turtle.done()

golden_rect_spiral(9, 6)
