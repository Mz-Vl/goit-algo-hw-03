import turtle


def snowflake(t, order, size):
    for i in range(3):
        koch_curve(t, order, size)
        t.right(120)


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 100)
    t.pendown()

    snowflake(t, order, size)

    window.mainloop()


recursion_level = int(input("Enter recursion level: "))
draw_koch_snowflake(recursion_level, 350)
