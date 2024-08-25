# plugins/date_plugin.py

from datetime import datetime
from plugin_abc import PluginABC

class DatePlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        gui.text_widget.clear()
        gui.text_widget.setText(f"Current Date and Time: {now}")

    def validate(self):
        return True

    def get_name(self):
        return "Tools:Date"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Display current date and time"

def register_plugin():
    return DatePlugin.register()