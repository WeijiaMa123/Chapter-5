import turtle
wn= turtle.Screen()
tess = turtle.Turtle()
tess.color("blue","red")
def ss(t,height,width):
    if height >= 0:
        t.beign_fill()
        t.left(90)
        t.forward(height)
        t.left(90)
        t.write(''+str(height))
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(50)
        t.pendown()
    else:
        t.left(90)
        t.forward(height)
        t.left(90)
        t.penup()
        t.forward(10)
        t.write(''+str(height))
        t.backward(10)
        t.pendown()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.penup()
        t.forward(50)
        t.pendown()
tess.penup()
tess.backward(200)
tess.pendown()

for i in [27,42,-15,31,-40,2]:
    ss(tess,i,10)
    
        
