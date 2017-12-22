#!/usr/bin/python3

""" This is the main module of the PythonTimer """

import sys
from PyQt5.QtWidgets import QApplication

from window import Window

def main():
    """ The main function.
    It opens the timer window.
    """
    app = QApplication(sys.argv)
    Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    