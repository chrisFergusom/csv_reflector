# plugins/rotate_plugin.py

import pandas as pd
from plugin_abc import PluginABC
from PyQt6.QtWidgets import QMessageBox
from data_operations import is_original_state, restore_original_dtypes
from file_operations import display_data_with_info

class RotatePlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        if gui.df is None:
            QMessageBox.information(gui, "Info", "Please load a CSV file first.")
            return

        if not hasattr(gui, 'original_columns'):
            gui.original_dtypes = gui.df.dtypes.to_dict()
            gui.original_columns = gui.df.columns.tolist()
            gui.original_df = gui.df.copy()

        # Rotate column names and data 180 degrees
        column_row = pd.DataFrame([gui.df.columns.tolist()], columns=gui.df.columns)
        temp_df = pd.concat([column_row, gui.df], ignore_index=True)
        gui.df = temp_df.iloc[::-1, ::-1].reset_index(drop=True)
        new_columns = gui.df.iloc[0].tolist()
        gui.df = gui.df.iloc[1:]
        gui.df.columns = [str(col) for col in new_columns]

        if is_original_state(gui):
            restore_original_dtypes(gui)

        display_data_with_info(gui)

    def validate(self):
        return True

    def get_name(self):
        return "Edit:Rotate"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Rotate the data 180 degrees"

def register_plugin():
    return RotatePlugin.register()