from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QThread

from stopwatch import Stopwatch
import threading, time

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.stopwatch = Stopwatch()
        self.initUI()
        self.updater = ValueUpdater(self)
        self.updater.start()
    
    def initUI(self):
        # Window properties
        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle('PythonTimer')
        
        # Label
        self.timer_label = QLabel(self)
        self.timer_label.setText(str(self.stopwatch.get_time()))
        
        # Push buttons
        self.start_button = QPushButton('Start / Pause', self)
        self.start_button.clicked.connect(self.start_pressed)
        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_pressed)
        
        # Layout

        label_row = QHBoxLayout()
        label_row.addStretch(1)
        label_row.addWidget(self.timer_label)
        label_row.addStretch(1)
        
        button_row = QHBoxLayout()
        button_row.addStretch(1)
        button_row.addWidget(self.start_button)
        button_row.addWidget(self.reset_button)
        button_row.addStretch(1)
        
        vert_layout = QVBoxLayout()
        vert_layout.addStretch(1)
        vert_layout.addLayout(label_row)
        vert_layout.addStretch(1)
        vert_layout.addLayout(button_row)
        
        self.setLayout(vert_layout)
        
        self.show()
    
    def start_pressed(self):
        self.stopwatch.start_or_pause()
        
    def reset_pressed(self):
        self.stopwatch.reset()
        

class ValueUpdater(QThread):

    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        while True:
            time.sleep(1)
            print(self.window.stopwatch.get_time())
            self.window.timer_label.setText(str(self.window.stopwatch.get_time()))
            self.window.timer_label.adjustSize()
            self.window.show()
    

        