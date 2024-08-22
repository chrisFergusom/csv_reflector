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

def track_button_press(button_name, button_log):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    button_log[timestamp] = button_name

def get_category(button, button_categories):
    for category, buttons in button_categories.items():
        if button in buttons:
            return category
    return 'Unknown'

def show_button_info(gui):
    track_button_press('Button Info', gui.button_log)
    df = pd.DataFrame.from_dict(gui.button_log, orient='index', columns=['Button'])
    print(df)
    df.index = pd.to_datetime(df.index)

    button_counts = df['Button'].value_counts()
    category_counts = df['Button'].map(lambda x: get_category(x, gui.button_categories)).value_counts()

    total_presses = len(df)
    gui.text_widget.clear()
    gui.text_widget.append(f"ALL TIME BUTTON PRESSES: {total_presses}\n")

    for category, buttons in gui.button_categories.items():
        category_total = category_counts.get(category, 0)
        gui.text_widget.append(f"**{category}**: {category_total}")
        for button in buttons:
            count = button_counts.get(button, 0)
            gui.text_widget.append(f"{button}: {count}")
        gui.text_widget.append("")

    show_charts(df, gui)