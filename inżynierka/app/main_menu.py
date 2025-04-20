from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from app.user_profile_window import UserProfileWindow
from app.quiz_window import QuizWindow

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Główne")
        self.setGeometry(200, 100, 1400, 800)

        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        mid_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        top_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        mid_layout.addItem(QSpacerItem(QSizePolicy.Expanding, QSizePolicy.Minimum))
        bottom_layout.addItem(QSpacerItem(QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.quiz_button = QPushButton("Rozpocznij Quiz")
        self.quiz_button.setFixedSize(150, 40)
        self.profile_button = QPushButton("Profil Użytkownika")
        self.profile_button.setFixedSize(150, 40)
        self.exit_button = QPushButton("Wyjście")
        self.exit_button.setFixedSize(150, 40)

        top_layout.addWidget(self.profile_button)
        mid_layout.addWidget(self.quiz_button)
        bottom_layout.addWidget(self.exit_button)

        self.profile_button.setStyleSheet("""
            QPushButton {
                background-color: #4472C4;
                color: cyan;
                font-weight: bold;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #5A9BD4;
            }
        """)


        self.quiz_button.clicked.connect(self.open_quiz)
        self.profile_button.clicked.connect(self.open_profile)
        self.exit_button.clicked.connect(self.close)


        layout.addLayout(top_layout)
        layout.addSpacing(300)
        layout.addLayout(mid_layout)
        layout.addSpacing(200)
        layout.addLayout(bottom_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_quiz(self):
        self.quiz_window = QuizWindow(self)
        self.quiz_window.show()
        self.hide()

    def open_profile(self):
        self.profile_window = UserProfileWindow(self)
        self.profile_window.show()
        self.hide()
