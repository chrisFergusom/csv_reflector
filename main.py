# main.py

import sys
from PyQt6.QtWidgets import QApplication
from gui import CSVGUI

def run_gui():
    app = QApplication(sys.argv)
    gui = CSVGUI()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_gui()