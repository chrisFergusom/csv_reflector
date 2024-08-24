# haiku_generator.py

import json
import random
from button_tracking import track_button_press

def load_haiku_words():
    with open('haiku.json', 'r') as f:
        return json.load(f)

def generate_haiku(gui):
    track_button_press('"Reflect"', gui.button_log)
    words = load_haiku_words()
    
    syllable_map = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    
    def get_word(syllables, word_type):
        syllable_key = syllable_map[syllables]
        word_list = words['syllables'][syllable_key][word_type]
        if word_list:
            word = random.choice(word_list)
            word_list.remove(word)
            return word
        return None

    def generate_line(target_syllables):
        line = []
        current_syllables = 0
        word_types = ['nouns', 'verbs', 'adjectives']
        
        while current_syllables < target_syllables:
            remaining_syllables = target_syllables - current_syllables
            possible_syllables = [s for s in range(1, 6) if s <= remaining_syllables]
            
            if not possible_syllables:
                break
            
            syllables = random.choice(possible_syllables)
            word_type = random.choice(word_types)
            
            word = get_word(syllables, word_type)
            if word:
                line.append(word)
                current_syllables += syllables
            
        return ' '.join(line)

    haiku_parts = []
    for _ in range(2):
        part = [
            generate_line(5),
            generate_line(7),
            generate_line(5)
        ]
        haiku_parts.append('\n'.join(part))

    gui.text_widget.clear()
    gui.text_widget.append("\n\nTwo-part Haiku Reflection:\n" + "\n\n".join(haiku_parts))