# plugins/example_plugin.py

from PyQt6.QtWidgets import QMessageBox

def run_plugin(gui):
    QMessageBox.information(gui, "Example Plugin", "This is an example plugin!")

def register_plugin():
    return {
        'name': 'Example Plugin',
        'description': 'An example plugin to demonstrate the plugin system',
        'version': '1.0',
        'run': run_plugin
    } 