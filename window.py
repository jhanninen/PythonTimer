from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(50, 50, 300, 200)
        self.qLabel = QLabel(self)
        self.qLabel.move(70, 120)
        self.qLabel.setText("Tähän tulee ajastin")
        self.__button = QPushButton('Push', self)
        self.setWindowTitle('Ajastin')
        self.show()
    