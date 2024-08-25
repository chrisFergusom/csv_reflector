# plugins/wikipedia_search_plugin.py

import requests
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import QInputDialog, QMessageBox
from plugin_abc import PluginABC

class WikipediaSearchPlugin(PluginABC):
    def __init__(self):
        pass

    def configure(self):
        pass

    def initialize(self):
        pass

    def shutdown(self):
        pass

    def execute(self, gui):
        search_term, ok = QInputDialog.getText(gui, 'Search Wikipedia', 'Enter search term:')
        if ok and search_term:
            try:
                url = f"https://en.wikipedia.org/wiki/{search_term.replace(' ', '_')}"
                response = requests.get(url)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                content = soup.find(id="mw-content-text").find(class_="mw-parser-output")
                
                gui.text_widget.clear()
                gui.text_widget.append(f"Wikipedia content for '{search_term}':\n\n")
                gui.text_widget.append(content.get_text())
            except requests.exceptions.RequestException:
                QMessageBox.warning(gui, "Error", f"No Wikipedia page found for '{search_term}'")

    def validate(self):
        return True

    def get_name(self):
        return "Tools:Wikipedia Search"

    def get_version(self):
        return "1.0"

    def get_description(self):
        return "Search Wikipedia for a given term"

def register_plugin():
    return WikipediaSearchPlugin.register()