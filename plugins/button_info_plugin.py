# plugins/button_info_plugin.py
from plugin_abc import PluginABC
from button_tracking import show_button_info

class ButtonInfoPlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        show_button_info(gui)

    def validate(self):
        return True

    def get_name(self):
        return "Info:Button Info"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Display button usage statistics and log"

def register_plugin():
    return ButtonInfoPlugin.register()