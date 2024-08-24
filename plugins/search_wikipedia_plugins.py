# plugins/search_wikipedia_plugin.py

import requests
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import QInputDialog, QMessageBox

def search_wikipedia(gui):
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

def run_plugin(gui):
    search_wikipedia(gui)

def register_plugin():
    return {
        'name': 'Wikipedia Search',
        'description': 'Search Wikipedia for a given term',
        'version': '1.0',
        'run': run_plugin
    }