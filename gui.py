from PyQt6.QtWidgets import QMainWindow, QTextEdit
from PyQt6.QtGui import QFont
from plugin_manager import PluginManager
from button_tracking import load_button_log, save_button_log, track_button_press

class CSVGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Reflector")
        self.button_log_file = 'data/button_log.json'
        self.button_log = load_button_log(self.button_log_file)
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins('plugins')
        self.df = None
        self.original_df = None
        self.button_categories = self.plugin_manager.button_categories
        self.create_text_widget()
        self.create_menu()
        self.show()

    def create_text_widget(self):
        self.text_widget = QTextEdit()
        self.courier_font = QFont("Courier")
        self.text_widget.setFont(self.courier_font)
        self.setCentralWidget(self.text_widget)

    def create_menu(self):
        menubar = self.menuBar()
        menubar.clear()

        self.menus = {}
        for menu_name, plugins in self.plugin_manager.get_all_plugins().items():
            self.menus[menu_name] = menubar.addMenu(menu_name)
            for plugin_name, plugin_info in plugins.items():
                action = self.menus[menu_name].addAction(plugin_name)
                action.triggered.connect(lambda checked, m=menu_name, n=plugin_name: self.run_plugin(m, n))

    def run_plugin(self, menu_name, plugin_name):
        plugin = self.plugin_manager.get_plugin(menu_name, plugin_name)
        if plugin and 'run' in plugin:
            track_button_press(f'{menu_name}:{plugin_name}', self.button_log, self.button_categories)
            plugin['run'](self)

    def save_button_log(self):
        save_button_log(self.button_log, self.button_log_file)