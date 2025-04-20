from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class UserProfileWindow(QMainWindow):
    def __init__(self, parent_menu):
        super().__init__()
        self.parent_menu = parent_menu
        self.setWindowTitle("Profil Użytkownika")
        self.setGeometry(200, 100, 1400, 800)

        layout = QVBoxLayout()
        label = QLabel("Profil")
        back_button = QPushButton("Powrót do menu")
        back_button.clicked.connect(self.back_to_menu)
        back_button.setFixedSize(150, 40)


        layout.addWidget(label)
        layout.addWidget(back_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def back_to_menu(self):
        self.parent_menu.show()
        self.close()
