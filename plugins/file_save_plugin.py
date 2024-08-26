# plugins/file_save_plugin.py
from plugin_abc import PluginABC
from file_operations import save_file

class FileSavePlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        save_file(gui)

    def validate(self):
        return True

    def get_name(self):
        return "File:Save"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Save the current dataframe to a file"

def register_plugin():
    return FileSavePlugin.register()