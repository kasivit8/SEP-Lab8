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

        self.anim_area = Animation_area()

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)

        self.setLayout(layout)
        self.setMinimumSize(530, 600)


def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())