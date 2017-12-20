#!/usr/bin/python3

import sys
from window import Window

from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    ui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    