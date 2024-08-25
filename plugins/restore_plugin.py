# plugins/restore_plugin.py

from plugin_abc import PluginABC
from PyQt6.QtWidgets import QMessageBox
from file_operations import display_data_with_info

class RestorePlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        if gui.original_df is not None:
            gui.df = gui.original_df.copy()
            display_data_with_info(gui)
        else:
            QMessageBox.information(gui, "Info", "No original data to restore.")

    def validate(self):
        return True

    def get_name(self):
        return "Edit:Restore"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Restore the dataframe to its original state"

def register_plugin():
    return RestorePlugin.register()