# button_tracking.py

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTextEdit
import json
from datetime import datetime
import pandas as pd
from chart_operations import show_charts

def load_button_log(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_button_log(button_log, filename):
    with open(filename, 'w') as f:
        json.dump(button_log, f)

def track_button_press(button_name, button_log, button_categories):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    button_log[timestamp] = button_name
    
    # Update button categories if it's a plugin
    if button_name.startswith('Plugin:'):
        category = 'Plugins'
        plugin_name = button_name.split(': ')[1]
        if 'Plugins' not in button_categories:
            button_categories['Plugins'] = []
        if plugin_name not in button_categories['Plugins']:
            button_categories['Plugins'].append(plugin_name)

def get_category(button, button_categories):
    for category, buttons in button_categories.items():
        if button in buttons:
            return category
    return 'Unknown'

def show_button_log_popup(gui):
    dialog = QDialog(gui)
    dialog.setWindowTitle("Button Log")
    layout = QVBoxLayout()
    text_edit = QTextEdit()
    text_edit.setFont(gui.courier_font)
    text_edit.setReadOnly(True)
    
    log_text = "\n".join([f"{timestamp}: {button}" for timestamp, button in gui.button_log.items()])
    text_edit.setText(log_text)
    
    layout.addWidget(text_edit)
    dialog.setLayout(layout)
    dialog.resize(400, 300)
    dialog.exec()

def show_button_info(gui):
    track_button_press('Button Info', gui.button_log, gui.button_categories)
    df = pd.DataFrame.from_dict(gui.button_log, orient='index', columns=['Button'])
    df.index = pd.to_datetime(df.index)

    # Separate plugin buttons from regular buttons
    plugin_df = df[df['Button'].str.startswith('Plugin:')]
    regular_df = df[~df['Button'].str.startswith('Plugin:')]

    regular_button_counts = regular_df['Button'].value_counts()
    plugin_button_counts = plugin_df['Button'].apply(lambda x: x.split(': ')[1]).value_counts()

    regular_category_counts = regular_df['Button'].map(lambda x: get_category(x, gui.button_categories)).value_counts()
    
    total_presses = len(df)
    gui.text_widget.clear()
    gui.text_widget.append(f"ALL TIME BUTTON PRESSES: {total_presses}\n")

    for category, buttons in gui.button_categories.items():
        if category != 'Plugins':
            category_total = regular_category_counts.get(category, 0)
            gui.text_widget.append(f"**{category}**: {category_total}")
            for button in buttons:
                count = regular_button_counts.get(button, 0)
                gui.text_widget.append(f"{button}: {count}")
            gui.text_widget.append("")

    # Handle plugin buttons
    plugin_total = len(plugin_df)
    gui.text_widget.append(f"**Plugins**: {plugin_total}")
    for plugin, count in plugin_button_counts.items():
        gui.text_widget.append(f"{plugin}: {count}")
    gui.text_widget.append("")

    show_charts(df, gui)
    show_button_log_popup(gui)