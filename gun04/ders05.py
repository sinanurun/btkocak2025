import turtle as t

t.speed(1) # 0, 10, 6 3 1
t.color("blue","red")

# loop for pattern
for i in range(10):
    # set turtle speed
    t.speed(10 - i)

    # motion for pattern
    t.forward(50 + 10 * i)
    t.right(90)

t.begin_fill()
for a in range(360):
    t.forward(3)
    t.left(1)
t.end_fill()

t.penup()

t.forward(50)
t.pendown()
t.color("blue","yellow")

t.begin_fill()
for a in range(360):
    t.forward(3)
    t.left(1)
t.end_fill()


t.mainloop()