# haiku_generator.py

import random
from button_tracking import track_button_press

def generate_haiku(gui):
    track_button_press('"Reflect"', gui.button_log)
    words = [
        ('Life', 'Hope', 'Faith', 'Love', 'Soul', 'Time', 'Heart', 'Dream', 'Mind', 'Peace'),
        ('wanders', 'searches', 'yearns', 'struggles', 'dreams', 'whispers', 'travels', 'echoes', 'dances', 'grows'),
        ('endlessly', 'constantly', 'silently', 'patiently', 'fearlessly', 'gracefully', 'carefully', 'peacefully', 'quietly', 'steadily'),
        ('through', 'in', 'with', 'for', 'amidst', 'beside', 'among', 'inside', 'beyond', 'within'),
        ('chaos', 'darkness', 'beauty', 'wonder', 'twilight', 'harmony', 'balance', 'laughter', 'sorrow', 'wisdom')
    ]

    used_words = set()
    haiku_parts = []
    for _ in range(2):
        available_words = [list(set(category) - used_words) for category in words]
        haiku_part = [
            f"{random.choice(available_words[0])} {random.choice(available_words[1])}",
            f"{random.choice(available_words[2])} {random.choice(available_words[3])} {random.choice(available_words[4])}",
            f"{random.choice(available_words[0])} {random.choice(available_words[1])}"
        ]
        haiku_parts = []
        for _ in range(2):  # Generate two haiku parts
            available_words = [list(set(category) - used_words) for category in words]
            haiku_part = [
                f"{random.choice(available_words[0])} {random.choice(available_words[1])}",
                f"{random.choice(available_words[2])} {random.choice(available_words[3])} {random.choice(available_words[4])}",
                f"{random.choice(available_words[0])} {random.choice(available_words[1])}"
            ]
            haiku_parts.append("\n".join(haiku_part))
            used_words.update(word for line in haiku_part for word in line.split())
        gui.text_widget.clear()
        gui.text_widget.append("\n\nTwo-part Haiku Reflection:\n" + "\n\n".join(haiku_parts))