import turtle as t
class Disk:
    def __init__(self,name,x,y,h,w,colour="blue"):
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

     def cleardisk(self):
        self.t.pendown()
        self.t.setheading(0)
        self.t.color("white")
        self.t.pencolor("white")
        self.t.begin_fill()
        self.t.fd(self.w / 2)
        self.t.left(90)
        self.t.fd(self.h)
        self.t.left(90)
        self.t.fd(self.w)
        self.t.left(90)
        self.t.fd(self.h)
        self.t.left(90)
        self.t.fd(self.w / 2)
        self.t.end_fill()
        self.t.penup()

    def newpos(self,x,y):
        self.x = x
@@ -88,32 +70,17 @@ def showpole(self):
        self.t.end_fill()
        self.t.penup()

class Hanoi(object):
    def __init__(self,n=3,start = "A",workspace = "B", destination = "C"):

        self.startp  = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*150,20,(n-1)*30))
    def pushdisk(self, disk):
        self.top += 1
        self.stack.append(disk)
        disk.newpos(self.x, (self.y+disk.height)*len(self.stack))

    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)
    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)
    def popdisk(self):
        disk = self.stack.pop()
        disk.newpos(self.x, self.length+50)
        self.top -= 1
        return disk


h = Hanoi()
h.solve() 