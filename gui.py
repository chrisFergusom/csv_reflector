# gui.py

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTextEdit, QMessageBox
from PyQt6.QtGui import QFont
import atexit
from collections import OrderedDict

from plugin_manager import PluginManager
from button_tracking import track_button_press, load_button_log, save_button_log, show_button_info
from file_operations import load_file, save_file
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
            ('Options', ['Text']),
            ('Info', ['About', 'Button Info']),
            ('Tools', [])
        ])
        self.button_log_file = 'data/button_log.json'
        self.button_log = load_button_log(self.button_log_file)
        atexit.register(self.save_button_log)
        
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins('plugins')
        self.create_menu()
        self.create_text_widget()
        self.show()

    def create_menu(self):
        menubar = self.menuBar()
        menubar.clear()

        self.menus = {
            "File": menubar.addMenu("File"),
            "Edit": menubar.addMenu("Edit"),
            "Options": menubar.addMenu("Options"),
            "Info": menubar.addMenu("Info"),
            "Tools": menubar.addMenu("Tools")
        }

        self.add_menu_items()

    def add_menu_items(self):
        standard_actions = {
            "File": [
                ("Load", lambda: load_file(self)),
                ("Save", lambda: save_file(self)),
                ("Exit", self.exit_application)
            ],
            "Options": [
                ("Text", lambda: apply_text_formatting(self))
            ],
            "Info": [
                ("About", self.show_about),
                ("Button Info", lambda: show_button_info(self))
            ]
        }

        # Add standard menu items
        for menu_name, actions in standard_actions.items():
            for action_name, action_func in actions:
                action = self.menus[menu_name].addAction(action_name)
                action.triggered.connect(lambda checked, n=action_name, f=action_func: self.run_action(n, f))

        # Add plugin menu items
        for menu_name, plugins in self.plugin_manager.get_all_plugins().items():
            if menu_name not in self.menus:
                self.menus[menu_name] = self.menuBar().addMenu(menu_name)
            
            for plugin_name, plugin_info in plugins.items():
                action = self.menus[menu_name].addAction(plugin_name)
                action.triggered.connect(lambda checked, m=menu_name, n=plugin_name: self.run_plugin(m, n))


    def run_action(self, action_name, action_func):
        track_button_press(action_name, self.button_log, self.button_categories)
        action_func()

    def run_plugin(self, menu_name, plugin_name):
        plugin = self.plugin_manager.get_plugin(menu_name, plugin_name)
        if plugin and 'run' in plugin:
            track_button_press(f'{menu_name}:{plugin_name}', self.button_log, self.button_categories)
            plugin['run'](self)

    def create_text_widget(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.text_widget = QTextEdit()
        self.courier_font = QFont("Courier")
        self.text_widget.setFont(self.courier_font)
        self.layout.addWidget(self.text_widget)

    def show_about(self):
        track_button_press('About', self.button_log, self.button_categories)
        about_message = "CSV Reflector\nVersion 1.0\n© 2024 MyCorp\nA tool for CSV manipulation and reflection."
        QMessageBox.information(self, "About", about_message)

    def save_button_log(self):
        save_button_log(self.button_log, self.button_log_file)

    def exit_application(self):
        track_button_press('Exit', self.button_log, self.button_categories)
        self.close()