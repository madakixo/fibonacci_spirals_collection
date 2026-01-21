import turtle

def fib_spiral_classic(n=12, scale=5):
    fib = [0, 1]
    for _ in range(n):
        fib.append(fib[-1] + fib[-2])
    fib = fib[1:]  # 1,1,2,3,5,...

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    turtle.bgcolor("black")
    t.pencolor("gold")
    t.pensize(2)

    directions = [0, 90, 180, 270]  # right, up, left, down
    dir_idx = 0

    for i, side in enumerate(fib):
        s = side * scale
        for _ in range(4):
            t.forward(s)
            t.left(90)

        t.penup()
        t.setheading(directions[dir_idx])
        t.forward(s)
        t.pendown()
        dir_idx = (dir_idx + 1) % 4

    turtle.done()

fib_spiral_classic(13, 6)
