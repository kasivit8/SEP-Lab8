import turtle as t

class Disk:
    def __init__(self,name,x,y,h,w,colour):
        self.name = name
        self.h = h
        self.w = w
        self.t = t.Turtle()
        self.color = colour
        self.x = x
        self.y = y
        self.t.penup()
        self.t.goto(x,y)
        

    def showdisk(self):
        self.t.pendown()
        self.t.setheading(0)
        self.t.color(self.color)
        self.t.pencolor("black")
        self.t.begin_fill()
        self.t.fd(self.w/2)
        self.t.left(90)
        self.t.fd(self.h)
        self.t.left(90)
        self.t.fd(self.w)
        self.t.left(90)
        self.t.fd(self.h)
        self.t.left(90)
        self.t.fd(self.w/2)
        self.t.end_fill()
        self.t.penup()

    def newpos(self,x,y):
        self.x = x
        self.y = y
        self.t.penup()
        self.t.goto(x,y)
