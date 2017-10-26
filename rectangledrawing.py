import turtle
wn= turtle.Screen()
sl= turtle.Turtle()
def ss(sl,height,width):
    for i in range(2):
        sl.forward(width)
        sl.left(90)
        sl.forward(height)
        sl.left(90)
    sl.penup()
    sl.forward(50)
    sl.pendown()
sl.penup()
sl.backward(200)
sl.pendown()
for i in [27,42,-15,31,-40,2]:
    ss(sl,i,10)
    
        
