# plugins/options_text_plugin.py
from plugin_abc import PluginABC
from text_formatting import apply_text_formatting

class OptionsTextPlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        apply_text_formatting(gui)

    def validate(self):
        return True

    def get_name(self):
        return "Options:Text"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Change the text formatting"

def register_plugin():
    return OptionsTextPlugin.register()