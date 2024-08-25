# plugins/reflect_plugin.py

from plugin_abc import PluginABC
from file_operations import display_data_with_info
from data_operations import is_original_state, restore_original_dtypes

class ReflectPlugin(PluginABC):
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

        gui.df = gui.df.iloc[:, ::-1]
        gui.df.columns = [str(col)[::-1] for col in gui.df.columns]
        gui.df = gui.df.astype(str).apply(lambda x: x.str[::-1])

        if is_original_state(gui):
            restore_original_dtypes(gui)

        display_data_with_info(gui)

    def validate(self):
        return True

    def get_name(self):
        return "Edit:Reflect"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Reflect the dataframe horizontally"

def register_plugin():
    return ReflectPlugin.register()