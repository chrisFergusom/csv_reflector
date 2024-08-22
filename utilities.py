from datetime import datetime

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_category(button, button_categories):
    for category, buttons in button_categories.items():
        if button in buttons:
            return category
    return 'Unknown'