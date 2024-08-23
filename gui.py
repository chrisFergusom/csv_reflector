# gui.py

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
import atexit
from collections import OrderedDict

from file_operations import load_file, save_file
from data_operations import reflect_data, flip_data, rotate_data, random_data, restore_data
from button_tracking import load_button_log, save_button_log, track_button_press, show_button_info
from haiku_generator import generate_haiku
from search_operations import search_wikipedia
from text_formatting import apply_text_formatting

class CSVGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Reflector")
        self.setGeometry(10, 10, 1600, 780)
        self.df = None
        self.rotate_count = 0
        self.original_dtypes = None
        self.button_categories = OrderedDict([
            ('File', ['Load', 'Save', 'Exit']),
            ('Edit', ['Reflect', 'Flip', 'Rotate', 'Random', 'Restore']),
            ('Options', ['Text']),  # Add this line
            ('Info', ['About', 'Date', '"Reflect"', 'Button Info', 'Search'])
        ])
        self.button_log_file = 'button_log.json'
        self.button_log = load_button_log(self.button_log_file)
        atexit.register(self.save_button_log)
        self.create_menu()
        self.create_text_widget()
        self.show()

    def create_menu(self):
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("File")
        load_action = file_menu.addAction("Load")
        load_action.triggered.connect(lambda: load_file(self))
        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(lambda: save_file(self))
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.exit_application)

        edit_menu = menubar.addMenu("Edit")
        reflect_action = edit_menu.addAction("Reflect")
        reflect_action.triggered.connect(lambda: reflect_data(self))
        flip_action = edit_menu.addAction("Flip")
        flip_action.triggered.connect(lambda: flip_data(self))
        rotate_action = edit_menu.addAction("Rotate")
        rotate_action.triggered.connect(lambda: rotate_data(self))
        random_action = edit_menu.addAction("Random")
        random_action.triggered.connect(lambda: random_data(self))
        restore_action = edit_menu.addAction("Restore")
        restore_action.triggered.connect(lambda: restore_data(self))

        options_menu = menubar.addMenu("Options")
        text_action = options_menu.addAction("Text")
        text_action.triggered.connect(lambda: apply_text_formatting(self))

        info_menu = menubar.addMenu("Info")
        about_action = info_menu.addAction("About")
        about_action.triggered.connect(self.show_about)
        date_action = info_menu.addAction("Date")
        date_action.triggered.connect(self.show_date)
        haiku_action = info_menu.addAction('"Reflect"')
        haiku_action.triggered.connect(lambda: generate_haiku(self))
        button_info_action = info_menu.addAction("Button Info")
        button_info_action.triggered.connect(lambda: show_button_info(self))
        search_action = info_menu.addAction("Search")
        search_action.triggered.connect(lambda: search_wikipedia(self))

    def create_text_widget(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.text_widget = QTextEdit()
        self.layout.addWidget(self.text_widget)

    def show_about(self):
        track_button_press('About', self.button_log)
        about_message = "CSV Reflector\nVersion 1.0\n© 2024 MyCorp\nA tool for CSV manipulation and reflection."
        QMessageBox.information(self, "About", about_message)

    def show_date(self):
        track_button_press('Date', self.button_log)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_widget.clear()
        self.text_widget.setText(f"Current Date and Time: {now}")

    def save_button_log(self):
        save_button_log(self.button_log, self.button_log_file)

    def exit_application(self):
        track_button_press('Exit', self.button_log)
        self.close()