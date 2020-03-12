# import sys
# from PySide2.QtCore import *
# from PySide2.QtWidgets import *
# from PySide2.QtGui import *
#
#
# class Animation_area(QWidget):
#     def __init__(self):
#         QWidget.__init__(self, None)
#         self.setMinimumSize(500, 500)
#
#         self.arena_w = 500
#         self.arena_h = 500
#
#
# class Simple_animation_window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self, None)
#
#         self.anim_area = Animation_area()
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.anim_area)
#
#         self.setLayout(layout)
#         self.setMinimumSize(530, 600)
#
#         self.b1 = QPushButton("Clear")
#         self.b1.toggle()
#         layout.addWidget(self.b1)
#         self.setWindowTitle("A simple paint program ")
#
#
#
#
# def main():
#     app = QApplication(sys.argv)
#     w = Simple_animation_window()
#     w.show()
#
#     return app.exec_()
#
#
# if __name__ == '__main__':
#     sys.exit(main())

# import turtle as t
#
#
# class Disk:
#     def __init__(self, name, x, y, h, w, colour="blue"):
#         self.name = name
#         self.h = h
#         self.w = w
#         self.t = t.Turtle()
#         self.color = colour
#         self.x = x
#         self.y = y
#         self.t.penup()
#         self.t.goto(x, y)
#
#     def showdisk(self):
#         self.t.pendown()
#         self.t.setheading(0)
#         self.t.color(self.color)
#         self.t.pencolor("black")
#         self.t.begin_fill()
#         self.t.fd(self.w / 2)
#         self.t.left(90)
#         self.t.fd(self.h)
#         self.t.left(90)
#         self.t.fd(self.w)
#         self.t.left(90)
#         self.t.fd(self.h)
#         self.t.left(90)
#         self.t.fd(self.w / 2)
#         self.t.end_fill()
#         self.t.penup()
#
#     def cleardisk(self):
#         self.t.pendown()
#         self.t.setheading(0)
#         self.t.color("white")
#         self.t.pencolor("white")
#         self.t.begin_fill()
#         self.t.fd(self.w / 2)
#         self.t.left(90)
#         self.t.fd(self.h)
#         self.t.left(90)
#         self.t.fd(self.w)
#         self.t.left(90)
#         self.t.fd(self.h)
#         self.t.left(90)
#         self.t.fd(self.w / 2)
#         self.t.end_fill()
#         self.t.penup()
#
#     def newpos(self, x, y):
#         self.x = x
#         self.y = y
#         self.t.penup()
#         self.t.goto(x, y)
#
#
# class Hanoi(object):
#     def __init__(self, n=3, start="A", workspace="B", destination="C"):
#
#         self.startp = Pole(start, 0, 0)
#         self.workspacep = Pole(workspace, 150, 0)
#         self.destinationp = Pole(destination, 300, 0)
#         self.startp.showpole()
#         self.workspacep.showpole()
#         self.destinationp.showpole()
#         for i in range(n):
#             self.startp.pushdisk(Disk("d" + str(i), 0, i * 150, 20, (n - 1) * 30))
#
#     def move_disk(self, start, destination):
#         disk = start.popdisk()
#         destination.pushdisk(disk)
#
#     def move_tower(self, n, s, d, w):
#         if n == 1:
#             self.move_disk(s, d)
#         else:
#             self.move_tower(n - 1, s, w, d)
#             self.move_disk(s, d)
#             self.move_tower(n - 1, w, d, s)
#
#     def solve(self):
#         self.move_tower(3, self.startp, self.destinationp, self.workspacep)
#
#
# h = Hanoi()
# h.solve()

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Paint")
        self.points = []

        self.resize(400, 400)

        self.label = QLabel(self)
        self.label.setText("Drag mouse to draw")
        self.label.move(140, 260)

        self.button = QPushButton(self)
        self.button.setText("Clear")
        self.button.move(140, 280)
        self.button.clicked.connect(self.clear_points)

    def clear_points(self):
        self.points.clear()

    def mouseMoveEvent(self, event):
        self.points.append(event.pos())

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(10, 10, 10))
        for point in self.points:
            p.drawPie(point.x(), point.y(), 10, 10, 0, 180 * 32)
        p.end()

        self.update()


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
