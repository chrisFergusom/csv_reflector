# plugins/file_load_plugin.py
from plugin_abc import PluginABC
from file_operations import load_file

class FileLoadPlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        load_file(gui)

    def validate(self):
        return True

    def get_name(self):
        return "File:Load"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Load a CSV, Excel or JSON file"

def register_plugin():
    return FileLoadPlugin.register()