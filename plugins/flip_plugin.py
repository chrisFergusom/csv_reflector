# plugins/flip_plugin.py

from plugin_abc import PluginABC
import pandas as pd
from file_operations import display_data_with_info
from data_operations import is_original_state, restore_original_dtypes

class FlipPlugin(PluginABC):
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
            return

        if not hasattr(gui, 'original_columns'):
            gui.original_dtypes = gui.df.dtypes.to_dict()
            gui.original_columns = gui.df.columns.tolist()

        column_row = pd.DataFrame([gui.df.columns.tolist()], columns=gui.df.columns)
        gui.df = pd.concat([column_row, gui.df], ignore_index=True)
        gui.df = gui.df.iloc[::-1].reset_index(drop=True)
        gui.df.columns = [str(val) for val in gui.df.iloc[0]]
        gui.df = gui.df.iloc[1:].reset_index(drop=True)

        if is_original_state(gui):
            restore_original_dtypes(gui)

        display_data_with_info(gui)

    def validate(self):
        return True

    def get_name(self):
        return "Edit:Flip"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Flip the dataframe vertically"

def register_plugin():
    return FlipPlugin.register()