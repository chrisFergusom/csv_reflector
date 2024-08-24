# plugins/word_count_plugin.py

from PyQt6.QtWidgets import QMessageBox

def run_plugin(gui):
    text = gui.text_widget.toPlainText()
    word_count = len(text.split())
    QMessageBox.information(gui, "Word Count", f"The text contains {word_count} words.")

def register_plugin():
    return {
        'name': 'Word Count',
        'description': 'Counts the number of words in the text widget',
        'version': '1.0',
        'run': run_plugin
    }