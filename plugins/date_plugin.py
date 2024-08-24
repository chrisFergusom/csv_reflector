# plugins/date_plugin.py

from PyQt6.QtWidgets import QMessageBox
from datetime import datetime

def run_plugin(gui):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gui.text_widget.clear()
    gui.text_widget.setText(f"Current Date and Time: {now}")

def register_plugin():
    return {
        'name': 'Date',
        'description': 'Display current date and time',
        'version': '1.0',
        'run': run_plugin
    }