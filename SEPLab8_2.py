import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(500,500)
        
        self.arena_w = 500
        self.arena_h = 500


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.points = QPolygon()

    def paintEvent(self, e):
        p = QPainter()
        p.setRenderHint(QPainter.Antialiasing)
        p.begin(self)
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,0,0))
        for point in self.points:
            #p.drawPoints(self.points)
            p.drawEllipse(point,15,10)
        p.end()

    def mouseMoveEvent(self, e):
        self.points << e.pos()
        self.update()


def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
