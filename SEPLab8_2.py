
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import *


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.anim_area = Animation_area()

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)

        self.button = QPushButton("Pause")
        self.button.clicked.connect(self.buttonClicked)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setMinimumSize(330,400)

    def buttonClicked(self):
        if(self.button.text() == "Pause"):
            self.button.setText("Play")
            self.anim_area.isPause = True
        else:
            self.button.setText("Pause")
            self.anim_area.isPause = False

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
