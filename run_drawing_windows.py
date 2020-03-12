import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Simple_drawing_window1 import Simple_drawing_window1
from Simple_drawing_window2 import Simple_drawing_window2
from Simple_drawing_window3 import Simple_drawing_window3

def main():
    app = QApplication(sys.argv)

    v = Simple_drawing_window1()
    v.show()
    w = Simple_drawing_window2()
    w.show()
    x = Simple_drawing_window3()
    x.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())