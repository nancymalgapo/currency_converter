import sys

from PyQt5.QtWidgets import QApplication

from components.application import RealTimeCurrencyConverter


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RealTimeCurrencyConverter()
    window.show()
    sys.exit(app.exec())
