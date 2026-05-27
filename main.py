# main.py
import sys
from PySide6.QtWidgets import QApplication
from views_visual import CounterWindow  
from logic import CounterLogic

class Controller:
    def __init__(self):
        self.view = CounterWindow()
        self.model = CounterLogic()
        self.cargar_estilos()

        # Conectamos las señales (UI) a la lógica (Backend)
        self.view.btn_up.clicked.connect(self.handle_increment)
        self.view.btn_down.clicked.connect(self.handle_decrement)

    def handle_increment(self):
        new_val = self.model.increment()
        self.view.label.setText(str(new_val))

    def handle_decrement(self):
        new_val = self.model.decrement()
        self.view.label.setText(str(new_val))

    def cargar_estilos(self):
        try:
            with open("styles.qss", "r") as f:
                self.view.setStyleSheet(f.read())
        except FileNotFoundError:
            pass

    def show(self):
        self.view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec())