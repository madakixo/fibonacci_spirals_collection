import turtle

def fib_spiral_colored(n=10, scale=8):
    fib = [1,1]
    for _ in range(n): fib.append(fib[-1]+fib[-2])

    t = turtle.Turtle()
    t.speed(0)
    turtle.bgcolor("black")
    t.hideturtle()

    colors = ['#ffbe0b','#fb5607','#ff006e','#8338ec','#3a86ff']

    for i, side in enumerate(fib):
        t.pencolor(colors[i % len(colors)])
        t.pensize(2.5 + i*0.4)

        for _ in range(4):
            t.forward(side * scale)
            t.left(90)

        # label
        t.penup()
        t.goto(t.pos() + (side*scale/3, side*scale/3))
        t.pencolor("white")
        t.write(f"F{i+1} = {side}", font=("Arial", 10, "bold"))
        t.pendown()

        # move to next position
        t.penup()
        t.forward(side * scale)
        t.right(90)
        t.pendown()

    turtle.done()

fib_spiral_colored(11, 7)
