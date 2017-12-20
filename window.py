from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Window properties
        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle('PythonTimer')
        
        # Label
        self.timer_label = QLabel(self)
        self.timer_label.setText("Tähän tulee ajastin")
        
        # Push buttons
        start_button = QPushButton('Start / Pause')
        reset_button = QPushButton('Reset')
        
        # Layout
        
        label_row = QHBoxLayout()
        label_row.addStretch(1)
        label_row.addWidget(self.timer_label)
        label_row.addStretch(1)
        
        button_row = QHBoxLayout()
        button_row.addStretch(1)
        button_row.addWidget(start_button)
        button_row.addWidget(reset_button)
        button_row.addStretch(1)
        
        vert_layout = QVBoxLayout()
        vert_layout.addStretch(1)
        vert_layout.addLayout(label_row)
        vert_layout.addStretch(1)
        vert_layout.addLayout(button_row)
        
        self.setLayout(vert_layout)
        
        self.show()
    