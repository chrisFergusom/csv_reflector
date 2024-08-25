# plugins/random_plugin.py

from plugin_abc import PluginABC
import numpy as np
from file_operations import display_data_with_info

class RandomPlugin(PluginABC):
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

        new_columns = gui.df.columns.tolist()
        np.random.shuffle(new_columns)
        scrambled_df = gui.df.copy()
        for col in scrambled_df.columns:
            scrambled_df[col] = scrambled_df[col].sample(frac=1).reset_index(drop=True)
        scrambled_df.columns = new_columns
        gui.df = scrambled_df

        display_data_with_info(gui)

    def validate(self):
        return True

    def get_name(self):
        return "Edit:Random"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Randomly scramble the dataframe"

def register_plugin():
    return RandomPlugin.register()