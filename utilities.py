# utilities.py

def get_category(button, button_categories):
    for category, buttons in button_categories.items():
        if button in buttons:
            return category
    return 'Unknown'