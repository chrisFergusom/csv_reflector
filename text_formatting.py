# text_formatting.py

from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QSpinBox, QCheckBox,
                             QPushButton, QLabel, QFontComboBox)
from PyQt6.QtGui import QTextCharFormat
from button_tracking import track_button_press

class TextFormattingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Text Formatting")
        self.setModal(True)
        self.layout = QVBoxLayout()

        # Font selection
        font_layout = QHBoxLayout()
        font_layout.addWidget(QLabel("Font:"))
        self.font_combo = QFontComboBox()
        font_layout.addWidget(self.font_combo)
        self.layout.addLayout(font_layout)

        # Font size
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Size:"))
        self.size_spin = QSpinBox()
        self.size_spin.setRange(1, 100)
        self.size_spin.setValue(12)
        size_layout.addWidget(self.size_spin)
        self.layout.addLayout(size_layout)

        # Style checkboxes
        self.bold_check = QCheckBox("Bold")
        self.italic_check = QCheckBox("Italic")
        self.underline_check = QCheckBox("Underline")
        self.layout.addWidget(self.bold_check)
        self.layout.addWidget(self.italic_check)
        self.layout.addWidget(self.underline_check)

        # OK and Cancel buttons
        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

    def get_format(self):
        font = self.font_combo.currentFont()
        font.setPointSize(self.size_spin.value())
        font.setBold(self.bold_check.isChecked())
        font.setItalic(self.italic_check.isChecked())
        font.setUnderline(self.underline_check.isChecked())
        return font

def apply_text_formatting(gui):
    track_button_press('Text', gui.button_log, gui.button_categories)
    dialog = TextFormattingDialog(gui)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        cursor = gui.text_widget.textCursor()
        if cursor.hasSelection():
            format = QTextCharFormat()
            format.setFont(dialog.get_format())
            cursor.mergeCharFormat(format)
        gui.text_widget.setTextCursor(cursor)