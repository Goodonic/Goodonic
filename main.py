# -*- coding: cp1251 -*-
from PyQt5.QtWidgets import *
import sys
from prog import *



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = prog()
    ex.show()
    app.exec_()