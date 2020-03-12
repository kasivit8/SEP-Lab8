import turtle as t

class Disk:
    def __init__(self,name,x,y,h,w):
        self.name = name
        self.h = h
        self.w = w
        self.t = t.Turtle()
        self.color = "blue"
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


class Pole:
    def __init__(self,name,x,y):
        self.name = name
        self.stack = []
        self.top_pos = 0
        self.x = x
        self.y = y
        self.thickness = 1
        self.length = 100
        self.color = "grey"
        self.t = t.Turtle()
        self.t.penup()
        self.t.goto(x,y)
    
    def showpole(self):
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

    def pushdisk(self, disk):
        self.top += 1
        self.stack.append(disk)
        disk.newpos(self.x, (self.y+disk.height)*len(self.stack))


    def popdisk(self):
        disk = self.stack.pop()
        disk.newpos(self.x, self.length+50)
        self.top -= 1
        return disk


        
