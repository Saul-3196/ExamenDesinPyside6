from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class CounterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Separated")

        # Elementos de la interfaz
        self.label = QLabel("0")
        self.btn_up = QPushButton("Incrementar")
        self.btn_down = QPushButton("Decrementar")

        # Layout (Organizador visual)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_up)
        layout.addWidget(self.btn_down)

        # Contenedor central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)