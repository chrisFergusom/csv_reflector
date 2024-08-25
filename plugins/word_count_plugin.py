# plugins/word_count_plugin.py

from PyQt6.QtWidgets import QMessageBox
from plugin_abc import PluginABC

class WordCountPlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        text = gui.text_widget.toPlainText()
        word_count = len(text.split())
        QMessageBox.information(gui, "Word Count", f"The text contains {word_count} words.")

    def validate(self):
        return True

    def get_name(self):
        return "Tools:Word Count"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Counts the number of words in the text widget"

def register_plugin():
    return WordCountPlugin.register()